# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 13

"""

def reg_multipla(x1, x2, y, tolerancia = 2e-9):
    n = len(x1)
    # y = a0 + a1x1 +a2x2

    Sx1 = Sx2 = Sx1x2 = Sx1Quad = Sx2Quad = Sy = Sx1y = Sx2y = 0

    for i in range(n):
        Sx1 += x1[i]
        Sx2 += x2[i]
        Sx1Quad += x1[i] * x1[i]
        Sx2Quad += x2[i] * x2[i]
        Sx1x2 += x1[i] * x2[i]
        Sy += y[i]
        Sx1y += x1[i] * y[i]
        Sx2y += x2[i] * y[i]

    A = [
        [n, Sx1, Sx2],
        [Sx1, Sx1Quad, Sx1x2],
        [Sx2, Sx1x2, Sx2Quad],
        ]
    
    C = [Sy, Sx1y, Sx2y]

    a = gauss_seidel(A, C, [0, 0, 0], tolerancia)

    # Soma dos quadrados dos resíduos estimados
    Sr = 0
    # Soma total dos quadrados em torno da média da variável dependente y
    St = 0
    # Média de y
    avg_y = np.average(y)

    for i in range(n):
        e = y[i] - a[0] - a[1] * x1[i] - a[2] * x2[i]
        Sr += e * e
        St += (y[i] - avg_y) * (y[i] - avg_y)

    # Coeficiente de Determinação
    r2 = (St - Sr) / St

    results = {
        "a0": a[0],
        "a1": a[1],
        "a2": a[2], 
        "r2": r2
        }
    
    print(results)

    return results

# Retorna um novo vetor ao "isolar" a variável da posição i
def isolar(i: int, v: object):
    new_v = np.array(v * (-1/v[i]), dtype= "float64")
    new_v[i] = 0.0
    return new_v

# Printa o vetor x
def print_x(v: object):
    for i in range(v.shape[0]):
        print(("x" + str(i + 1) + " ≈"), v[i])

# Retorna uma solução x para o sistema Ax = c usando o método de gauss_seidel
def gauss_seidel(A, c, x, tolerancia):
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

    return x


x1 = [1250, 1300, 1350, 1250, 1300, 1250, 1300, 1350, 1350]
x2 = [   6,    7,    6,    7,    6,    8,    8,    7,    8]
y =  [  80,   95,  101,   85,   92,   87,   96,  106,  108]

"""
ex_x1 = [0,  2, 2.5, 1, 4,  7]
ex_x2 = [0,  1,   2, 3, 6,  2]
ex_y =  [5, 10,   9, 0, 3, 27]
"""

reg_multipla(x1, x2, y)


