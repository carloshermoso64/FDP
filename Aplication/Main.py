# Filename: Main.py
# Author: Carlos Hermoso



from numpy import *
import matplotlib.pyplot as plt
import timeit
from Optimization import VIKOR_method

# performances of the alternatives
from Optimization.VIKOR_method import *

x = array([[5000, 937, 1, 2350, 20, 1.470, 1929936],
          [10000, 937, 1, 2350, 20, 1.470, 3216560],
          [25000, 937, 1, 2350, 20, 1.510, 9649680],
          [5000, 1.500, 1.5, 3100, 25, 1.450, 472812],
          [20000, 700, 2, 2000, 25, 0.700, 255490],
          [35000, 601, 2.5, 2000, 25, 0.600, 255490],
          [50000, 5.000, 2, 2596, 25, 4.200, 482856],
          [5000, 1.803, 1, 7500, 15, 5.425, 2524643],
          [5000, 1.803, 1, 7500, 15, 5.425, 2524643],
          [5000, 1.803, 1, 7500, 15, 2.813, 2524643],
          [56000, 856, 1, 7500, 20, 4.560, 4839548],
          [5000, 1.803, 1, 7500, 15, 7.106, 2524643],
          [2000, 1.503, 1.5, 7000, 20, 2.512, 5905270]])


# weights of the criteria
w = array([0.32, 0.09, 0.03, 0.12, 0.13, 0.04, 0.27])

# criteria max/min
crit_max_min = array(['max', 'min', 'min', 'max', 'max', 'min', 'max'])


n= vikor_ranking(x,crit_max_min,w)

print (n)