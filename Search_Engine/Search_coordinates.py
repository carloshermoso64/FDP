import requests
import json

key = ""
address = "New+york+Airport"

url = "https://maps.googleapis.com/maps/api/geocode/json?address="+ address +"&key=" + key

response = requests.request("GET", url)
json_data = json.loads(response.text)
print(json.dumps(json_data, indent=4, sort_keys=True))