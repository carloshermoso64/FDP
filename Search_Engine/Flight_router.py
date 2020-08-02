import requests
import json
import numpy
from numpy import *



def API_SkyScanner(origin,destination,outbound_date,inbound_date):

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/ES/EUR/es-ES/"+ origin +"/"+ destination +"/"+ outbound_date

    querystring = {"inboundpartialdate": inbound_date}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    print(json.dumps(json_data, indent=4, sort_keys=True))

    return json_data

def add_data_to_matrix(json_data,outbound_date):

    quotes = json_data["Quotes"]
    Matrix = ones((len(quotes),3))

    # AIRLINES:

    #carriers = json_data["Carriers"]
    #carrierId = []
    # carrierId.append(carriers[i]['CarrierId'])
    #  carrierId.append(quotes[i]['OutboundLeg']['CarrierIds'][0])
    # print (quotes[1]['OutboundLeg']['CarrierIds'][0])

    # DATES:

    out_date = outbound_date.split("-")
    out_year = out_date[0]
    out_month = out_date[1]
    out_day = out_date[2]

    for i in range(len(quotes)):

        # DATES:
        date = quotes[i]['OutboundLeg']['DepartureDate']
        x = date.split("-")
        year = x[0]
        month = x[1]
        day = x[2].split("T")
        day = day[0]
        delta_days = abs(int(day) - int(out_day))

        Matrix[i,0]=quotes[i]['MinPrice']
        Matrix[i,2]=delta_days

    print (Matrix)
    return Matrix

def flight_search(origin,destination,outbound_date,inbound_date):

    SkyScanner_data = API_SkyScanner(origin,destination,outbound_date,inbound_date)
    Matrix = add_data_to_matrix(SkyScanner_data,outbound_date)

    return Matrix

