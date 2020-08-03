import requests
import json

def API_Google_Directions_trip_search(origin,destination):

    key = ""

    url = "https://maps.googleapis.com/maps/api/directions/json?origin="+ origin +"&destination="+ destination +"&key="+ key

    response = requests.request("GET", url)
    json_data = json.loads(response.text)
    print(json.dumps(json_data, indent=4, sort_keys=True))


    long_distance = False

    routes = json_data["routes"]
    legs = routes[0]["legs"]

    #metros
    distance = legs[0]["distance"]["value"]

    #segundos
    duration =  legs[0]["duration"]["value"]

    start_address = legs[0]["start_address"]
    start_address_split = start_address.split(", ")
    origin_city = start_address_split[-2]

    end_address = legs[0]["end_address"]
    end_address_split = end_address.split(", ")
    destination_city = end_address_split[-2]


    if distance>300000:
        long_distance=True

    print(distance)
    print(duration)
    print(long_distance)
    print(origin_city)
    print(destination_city)

    return distance,duration,long_distance,origin_city,destination_city