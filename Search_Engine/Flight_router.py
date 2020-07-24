import requests
import json

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/SFO-sky/ORD-sky/2020-09-01"

querystring = {"inboundpartialdate":"2020-12-01"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "70b5b165e3msha89113c1ca22f72p146d2fjsn19ec9a108282"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_data = json.loads(response.text)
carriers = json_data["Carriers"]
#print(json.dumps(json_data,indent=4,sort_keys=True))
print(carriers)

i=0
carrierId = []
while i < len(carriers):
    print(carriers[i]['CarrierId'])
    carrierId.append(carriers[i]['CarrierId'])
    i += 1
print (carrierId)