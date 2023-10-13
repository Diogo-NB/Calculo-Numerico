# -*- coding: utf-8 -*-
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 8

"""

# Retorna um novo vetor ao "isolar" a variável da posição i
def isolar(i: int, v: object):
    new_v = np.array(v * (-1/v[i]), dtype= "float64")
    new_v[i] = 0.0
    return new_v

# Printa o vetor x
def print_x(v: object):
    for i in range(v.shape[0]):
        print(("x" + str(i + 1) + " ≈"), v[i])

A = [
    [8, -3, 2, 1, 0, -1], 
    [0, -10, 1, 1, -2, -1/2],
    [1, 0, 9, -1, 1, -3],
    [-2, 1, 0, -11, 1, 3/2],
    [-2, 0, 2, 0, 10, -2]
    ]
x = [0, 0, 0, 0, 0]

'''
A = [
    [2, 1, -20],
    [1, 4, -45]
    ]
x = [0, 0]
'''
 
tolerancia = 0.02
mr = 1

A = np.array(A, dtype="float64")
x = np.array(x, dtype="float64")

# Número de linhas 
nl = A.shape[0]
# Número de colunas para a matriz C
nc = nl

C = np.zeros((nl, nc))
g = np.zeros(nl)

# Encontrando a matriz C e o vetor g
for i in range(nl):
    aux = isolar(i, A[i])
    for j in range(nc):
        C[i][j] = aux[j]
    g[i] = aux[nc]

# Contador
k = 0

# Iterando
while mr > tolerancia:
    x_anterior = np.copy(x) # Vetor x da iteração anterior

    # Nova estimação de x: x = Cx + g
    x = np.dot(C, x) + g

    # Cálculo vetor m
    m = abs(x - x_anterior)

    # Calculo de erro
    mr = max(m).any() / max(x).any()

    k+=1 # Incrementando contador

print_x(x)

'''
x_real = np.array([19.0/1489.0, -44.0/1489.0, 991.0/2978.0, 214.0/1489.0, 405.0/2978.0])
print(x_real - x)

t = list(x)
t.append(1)
print(np.dot(A, t))   
'''