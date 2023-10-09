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
    # y = a0 + a1x +a2x^2

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

    a = gauss_seidel(A, C, [0, 0, 0], 0.000000002)

    # Soma dos quadrados dos resíduos estimados
    Sr = 0
    # Soma total dos quadrados em torno da média da variável dependente y
    St = 0
    # Média de y
    avg_y = np.average(y)

    for i in range(n):
        e = y[i] - a[0] - a[1] * (x[i]) - a[2] * (x[i]*x[i])
        Sr += e * e
        St += (y[i] - avg_y) * (y[i] - avg_y)

    y_calculado = np.zeros(n)
    
    for i in range(n):
        y_calculado[i] = a[0] + a[1]*(x[i]) + a[2] * (x[i] * x[i])

    plt.plot(x, y, 'o', color='black')
    plt.plot(x, y_calculado, color='red')
    plt.show()

    # Coeficiente de Determinação
    r2 = (St - Sr) / St

    results = {
        "a0": a[0],
        "a1": a[1],
        "a2": a[2], 
        "r2": r2
        }
    
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

# Ax = c
def gauss_seidel(A, c, x, tolerancia):
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
        print(m)
        # Calculo de erro
        mr = max(m) / max(x)
        
        k+=1 # Incrementando contador

    print("Número de iterações =", k)
    print_x(x)
    return x

x = [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
y = [ 87,  74,  62,  59,  65,  71,   82,   94]

ex_x = [1.5,  3, 4.5,   6,  7.5,   9,  10.5,   12]
ex_y = [ 87, 74,  62,  59,   65,   71,   82,   94]

print(reg_polinomial(ex_x, ex_y))
