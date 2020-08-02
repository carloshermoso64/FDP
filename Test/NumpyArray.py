import numpy
from numpy import *
import datetime

#m = zeros((3,2))

#n = ones((3,1))

#o = numpy.hstack((m,n))

#a = array((3,2))


#o = numpy.delete(o, 1, axis=1)
#print(o)

#base = datetime.datetime.today()
#print(base)

#o = o.transpose()

#x = numpy.hstack((o,a))


w, h = 8, 5;
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[0][0] = 1
Matrix[1][1] = 3
Matrix[2][5] = 4
Matrix[3][2] = 12
Matrix[4][7] = 9
Matrix[0][6] = 3

print(Matrix)