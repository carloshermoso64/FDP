# Filename: VIKOR_method
# Author: Carlos Hermoso
# References: J.R. San Cristóbal, Papathanasiou, J. & Ploskas, N.


from numpy import *

import scipy.stats as ss


#Step 1: Determine the best and worst values of all criterion

def best_worst_f(matrix, min_max_criteria):

    f = zeros((min_max_criteria.shape[0], 2))
    for i in range(min_max_criteria.shape[0]):
        if min_max_criteria[i] == 'max':
            f[i, 0] = matrix.max(0)[i]
            f[i, 1] = matrix.min(0)[i]
        elif min_max_criteria[i] == 'min':
            f[i, 0] = matrix.min(0)[i]
            f[i, 1] = matrix.max(0)[i]
    return f

#Step 2: Compute the values S and R

def S_and_R(matrix, best_worst_fij, weights):

    s = zeros(matrix.shape[0])
    r = zeros(matrix.shape[0])
    for i in range(matrix.shape[0]):
        k = 0
        o = 0
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

def vikor_ranking(matrix, min_max_criteria, weights):

    s, r = S_and_R(matrix,best_worst_f(matrix,min_max_criteria), weights)
    q = Q(s, r, len(weights))
    rank = ss.rankdata(-1*q)

    return rank, q