# -*- coding: utf-8 -*-
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 8

"""

def testSolution(A, x):
    x = list(x)
    x.append(1)
    print(A.dot(x))

# Retorna um novo vetor ao "isolar" a variável da posição i
def isolar(i: int, v: object):
    new_v = v * (-1/v[i])
    new_v[i] = 0
    return new_v

# Printa o vetor x
def print_x(v: object):
    for i in range(v.shape[0]):
        print("x" + str(i + 1) + " = " + str(v[i]))

A = [
    [8, -3, 2, 1, 0, -1], 
    [0, -10, 1, 1, -2, -1/2],
    [1, 0, 9, -1, 1, -3],
    [-2, 1, 0, -11, 1, 3/2],
    [-2, 0, 2, 0, 10, 2]
    ]
x = [0, 0, 0, 0, 0]

x_anterior = x
tolerancia = 0.02
mr = 1

A = np.array(A, dtype = np.double)
x = np.array(x, dtype = np.double)

# Shape = (nº de linhas, nº de colunas)
nl = A.shape[0] # nº de linhas
nc = A.shape[1] # nº de colunas

# Matriz C: Matriz A sem as constantes
C = np.zeros((nl, nc - 1), dtype = np.double)
# Vetor g: constantes da matriz A
g = np.zeros(nl, dtype = np.double)

# Obter C e g
for i in range(nl):
    aux = isolar(i, A[i])
    for j in range(nc - 1):
        C[i][j] = aux[j]
    g[i] = aux[nc-1]

# Iterando
while mr > tolerancia:
    x = C.dot(x_anterior) + g
    m = max(abs(x - x_anterior))
    mr = m / max(x)
    x_anterior = x

print(x)
print_x(x)

testSolution(A, x)









    




    