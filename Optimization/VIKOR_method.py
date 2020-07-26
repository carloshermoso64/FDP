# Filename: VIKOR_method.py
# Author: Carlos Hermoso
# References: J.R. San Cristóbal, Papathanasiou, J. & Ploskas, N.
import numpy as np
from numpy import *
import scipy.stats as ss


#Step 1: Determine the best and worst values of all criterion
#Also remove a column from the matrix if it has te same value for all the alternatives

def best_worst_f(matrix, min_max_criteria, weights):

    f = zeros((min_max_criteria.shape[0], 2))
    for i in range(min_max_criteria.shape[0]):
        if min_max_criteria[i] == 'max':
            f[i, 0] = matrix.max(0)[i]
            f[i, 1] = matrix.min(0)[i]
        elif min_max_criteria[i] == 'min':
            f[i, 0] = matrix.min(0)[i]
            f[i, 1] = matrix.max(0)[i]

        if f[i, 0] == f[i, 1]:
            matrix = np.delete(matrix, i, axis=1)
            weights = np.delete(weights, i)
            min_max_criteria = np.delete(min_max_criteria, i)

    return f, matrix, weights, min_max_criteria

#Step 2: Compute the values S and R

def S_and_R(matrix, best_worst_fij, weights):

    s = zeros(matrix.shape[0])
    r = zeros(matrix.shape[0])
    for i in range(matrix.shape[0]):
        k = 0.0
        o = 0.0
        for j in range(matrix.shape[1]):
            k = k + weights[j] * (best_worst_fij[j, 0] - matrix[i, j]) \
                    / (best_worst_fij[j, 0] - best_worst_fij[j, 1])
            u = weights[j] * (best_worst_fij[j, 0] - matrix[i, j]) \
                / (best_worst_fij[j, 0] - best_worst_fij[j, 1])
            if u > o:
                o = u
                r[i] = round(o, 3)
            else:
                r[i] = round(o, 3)
        s[i] = round(k, 3)
    return s, r

#Step 3: Compute the value Q

def Q(s, r, n):

    q = zeros(s.shape[0])
  #  y = ((n + 1) / (2 * n))
    y = 0.5
    for i in range(s.shape[0]):
        q[i] = round((y * (s[i] - min(s)) / (max(s) - min(s)) +
                 (1 - y) * (r[i] - min(r)) / (max(r) - min(r))), 3)
    return q

#Step 4: Rank the alternatives of the matrix

def vikor_ranking(matrix, min_max_criteria, weights):
    f, finalmatrix, finalweights, final_min_max_criteria = best_worst_f(matrix, min_max_criteria, weights)
    s, r = S_and_R(finalmatrix, f, finalweights)
    q = Q(s, r, len(weights))
    rank = ss.rankdata(q, method='ordinal')
    rank = tie_brake(rank, finalweights, finalmatrix) #look for alternatives with same value of q
    return rank

def tie_brake(rank, weights, matrix):

    result = []
    indx = []
    for i,item in enumerate(rank):
        dec,integer = math.modf(item)
        if (dec > 0.0):
            result.append(int(integer))
            indx.append(i)
    if result:
        j = 0
        while j < len(result):
            k = 0
            found = False
            while k < len(result) and not found:
                if result[k] == result[j] and k != j:
                    found=True
                else:
                    k = k+1
            if k != len(result):
                best,worst = compare(matrix, indx[j], indx[k], weights)
                rank[best] = rank[best]+0.5
                rank[worst] = rank[worst]-0.5
            result = np.delete(result, [j,k])
            indx = np.delete(indx, [j,k])

            j = 0
    return rank





def compare(matrix, a, b, weights):

    maxweight = np.where(weights == np.amax(weights))
    j = matrix[a, maxweight]
    k = matrix[b, maxweight]
    if j >= k:
        best = a
        worst = b
    else:
        best = b
        worst = a
    return best,worst

