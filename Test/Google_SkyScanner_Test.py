# Author: Carlos Hermoso


from Optimization.VIKOR_method import *
from Search_Engine.Flight_router import *
from Search_Engine.Road_router import *

origin = "Castelldefels"
destination = "Leganes"
outbound_date = "2020-09-17"
inbound_date = "2020-09-16"


distance,duration,long_distance,origin_city,destination_city=API_Google_Directions_trip_search(origin,destination)
origin_IATA_code = API_SkyScanner_IATA_code(origin_city)
destination_IATA_code = API_SkyScanner_IATA_code(destination_city)

origin_sky = origin_IATA_code+"-sky"
destination_sky = destination_IATA_code+"-sky"

xx= flight_search(origin_sky,destination_sky,outbound_date,inbound_date)
yy = array(['min', 'max', 'min'])
ww = array([0.5, 0.1, 0.4])

n = vikor_ranking(xx, yy, ww)


print(n)