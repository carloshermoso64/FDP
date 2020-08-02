import requests
import json
import numpy
from numpy import *


def flight_search():

    origin = "BCN-sky"
    destination = "AMS-sky"
    outbound_date = "2020-09-02"
    inbound_date = "2020-09-16"
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/ES/EUR/es-ES/"+ origin +"/"+ destination +"/"+ outbound_date

    querystring = {"inboundpartialdate": inbound_date}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    carriers = json_data["Carriers"]
    quotes = json_data["Quotes"]
    print(json.dumps(json_data,indent=4,sort_keys=True))

    i=0
    carrierId = []
    MinPrice = ones((len(quotes),3))
    DepartureDate = []
    DepartureDay = []
    DepartureMonth = []
    DepartureYear = []
   # print (quotes[i]['OutboundLeg']['DepartureDate'])

    out_date = outbound_date.split("-")
    out_year = out_date[0]
    out_month = out_date[1]
    out_day = out_date[2]



       # carrierId.append(carriers[i]['CarrierId'])
      #  carrierId.append(quotes[i]['OutboundLeg']['CarrierIds'][0])


    for i in range(len(quotes)):

        MinPrice[i,0]=quotes[i]['MinPrice']

        date = quotes[i]['OutboundLeg']['DepartureDate']
        x = date.split("-")
        year = x[0]
        month = x[1]
        day = x[2].split("T")
        day = day[0]
        DepartureDay.append(day)
        DepartureMonth.append(month)
        DepartureYear.append(year)

       # print(day)

        delta_days = abs(int(day) - int(out_day))

        MinPrice[i,2]=delta_days

    print (MinPrice)



    #print (quotes[1]['OutboundLeg']['CarrierIds'][0])




    return MinPrice

