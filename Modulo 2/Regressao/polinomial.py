# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 12

"""
def reg_polinomial(x, y):
    n = len(x)

    sx = sy = sx2 = sx3 = sx4 = sxy = sx2y = 0

    for i in range(n):
        x2 = x[i] ** 2 #x²

        sx += x[i]
        sy += y[i]
        sx2 += x2
        sx3 += x2 * x[i]
        sx4 += x2 * x2
        sxy += x[i] * y[i]
        sx2y += x2*y[i]

    A = [
        [n, sx, sx2],
        [sx, sx2, sx3],
        [sx2, sx3, sx4],
        ]
    
    C = [sy, sxy, sx2y]

    return (A, C)

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
while mr >= tolerancia:
    x_anterior = np.copy(x) # Vetor x da iteração anterior

    # Nova estimação de x: x = Cx + g
    for i in range(nl):
        x[i] = np.dot(C[i], x) + g[i]

    print(x)

    # Cálculo vetor m
    m = abs(x - x_anterior)
    print(m)
    # Calculo de erro
    mr = max(m) / max(x)
    
    k+=1 # Incrementando contador

print("Número de iterações =", k)
print_x(x)
