import numpy
from numpy import *

m = zeros((3,2))

n = ones((3,1))

o = numpy.hstack((m,n))

print(o)

o = numpy.delete(o, 1, axis=1)
print(o)
