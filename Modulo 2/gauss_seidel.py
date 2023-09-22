# -*- coding: utf-8 -*-
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 9

"""

# Retorna um novo vetor ao "isolar" a variável da posição i
def isolar(i: int, v: object):
    new_v = v * (-1/v[i])
    new_v[i] = 0
    return new_v

# Printa o vetor x
def print_x(v: object):
    for i in range(v.shape[0]):
        print(("x" + str(i + 1) + " ≈"), v[i])

# Exemplo 2
'''
A = [
    [3, -0.1, -0.2, -7.85],
    [0.1, 7, -0.3, 19.3],
    [0.3, -0.2, 10, -71.4]
    ]
'''
x = [0, 0, 0]

A = [
    [8, -3, 2, 1, 0, -1], 
    [0, -10, 1, 1, -2, -1/2],
    [1, 0, 9, -1, 1, -3],
    [-2, 1, 0, -11, 1, 3/2],
    [-2, 0, 2, 0, 10, 2]
    ]
x = [0, 0, 0, 0, 0]

tolerancia = 0.02
mr = 1

A = np.array(A, dtype = np.double)
x = np.array(x, dtype = np.double)

# A.shape = (nº de linhas de A, nº de colunas de A)
nl = A.shape[0] # nº de linhas de A

# Matriz C: Matriz A sem as constantes
nc = A.shape[1] - 1 # nº de colunas de C
C = np.zeros((nl, nc), dtype = np.double)
# Vetor g: constantes da matriz A
g = np.zeros(nl, dtype = np.double)

# Obter C e g
for i in range(nl):
    aux = isolar(i, A[i])
    for j in range(nc):
        C[i][j] = aux[j]
    g[i] = aux[nc]

# Iterando
while mr > tolerancia:
    x_anterior = np.array(x)
    #x = C.dot(x_anterior) + g
    for i in range(nl):
        x[i] = C[i].dot(x) + g[i]

    print(x)
    m = max(abs(x - x_anterior))
    mr = m / max(x)


print("x =", x)
print_x(x)

# Testar solução
x = list(x)
x.append(1)
print(A.dot(x))
 









    




    