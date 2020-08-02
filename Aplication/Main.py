# Filename: Main.py
# Author: Carlos Hermoso

from Optimization.VIKOR_method import *
from Search_Engine.Flight_router import *

origin = "BCN-sky"
destination = "AMS-sky"
outbound_date = "2020-09-02"
inbound_date = "2020-09-16"

#First column: Price of trip
#Second column: Type of transport
#Third colummn: Variation of days with desired date

xx= flight_search(origin,destination,outbound_date,inbound_date)
yy = array(['min', 'max', 'min'])
ww = array([0.5, 0.1, 0.4])

n = vikor_ranking(xx, yy, ww)


print(n)

