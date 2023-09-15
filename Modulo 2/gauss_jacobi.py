# -*- coding: utf-8 -*-
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 8

"""

def isolar(i, v):
    #res = -v/v[i]
    res = -v / v[i]
    res[i] = 0
    return res

A = np.array([[2,1,-20],[1,4,-45]])
C = np.zeros(A.shape)
G = np.zeros(A.shape[0])

qtdL = A.shape[0]
qtdC = A.shape[1]

for i in range(qtdL):
    G[i] = A[i][A.shape[1] -1]
    print(G[i])



# Shape = (l, c)


    




    