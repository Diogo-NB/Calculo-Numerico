# -*- coding: utf-8 -*-
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 9

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

def gauss_seidel(A, c, x, tolerancia, showResult = True):
    # Ax = c
    # Parametro x é a estimativa inicial de solução para x 
    mr = 1

    A = np.array(A, dtype="float64")
    c = np.array(c, dtype="float64")
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
        g[i] = c[i] / A[i][i]

    # Contador
    k = 0

    # Iterando
    while mr >= tolerancia:
        x_anterior = np.copy(x) # Vetor x da iteração anterior

        # Nova estimação de x: x = Cx + g
        for i in range(nl):
            x[i] = np.dot(C[i], x) + g[i]

        # Cálculo vetor m
        m = abs(x - x_anterior)
        
        # Calculo de erro
        mr = max(m) / max(x)
        
        k+=1 # Incrementando contador

    if (showResult):
        print("Número de iterações =", k)
        print_x(x)

    return x

A = [
    [8, -3, 2, 1, 0], 
    [0, -10, 1, 1, -2],
    [1, 0, 9, -1, 1],
    [-2, 1, 0, -11, 1],
    [-2, 0, 2, 0, 10]
    ]
c = [1, 1/2, 3, -3/2, 2]
x = [0, 0, 0, 0, 0]

gauss_seidel(A, c, x, 0.02)

"""
#Exemplo 2
ex_A = [
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
]
ex_c = [7.85, -19.3, 71.4]
ex_x_inicial = [0, 0, 0]
gauss_seidel(ex_A, ex_c, ex_x_inicial, 0.02)
"""