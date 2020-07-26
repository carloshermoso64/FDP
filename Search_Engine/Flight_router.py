import requests
import json
import numpy
from numpy import *


def flight_search():

    origin = "BCN-sky"
    destination = "JFK-sky"
    outbound_date = "2020-08-01"
    inbound_date = "2020-08-03"
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/"+ origin +"/"+ destination +"/"+ outbound_date

    querystring = {"inboundpartialdate": inbound_date}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    carriers = json_data["Carriers"]
    quotes = json_data["Quotes"]
    # print(json.dumps(json_data,indent=4,sort_keys=True))

    i=0
    carrierId = []
    MinPrice = ones((len(quotes),2))


       # carrierId.append(carriers[i]['CarrierId'])
      #  carrierId.append(quotes[i]['OutboundLeg']['CarrierIds'][0])


    for i in range(len(quotes)):
        MinPrice[i,0]=quotes[i]['MinPrice']
    #print (quotes[1]['OutboundLeg']['CarrierIds'][0])
    print(MinPrice)

    return MinPrice

