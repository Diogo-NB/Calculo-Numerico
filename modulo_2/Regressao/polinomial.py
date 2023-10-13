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

    a = gauss_seidel(A, C, [0, 0, 0], 2e-8)

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

    # Coeficiente de Determinação
    r2 = (St - Sr) / St

    results = {
        "a0": a[0],
        "a1": a[1],
        "a2": a[2], 
        "r2": r2
        }
    
    print(results)
    
    # Vetores de auxilio para melhor visualização
    l = 200 # Tamanho do vetor linspace
    x_aux = np.linspace(x[0], x[n - 1] , l).astype(float)
    y_aux = np.zeros(l)

    for i in range(l):
        y_aux[i] = a[0] + a[1]*(x_aux[i]) + a[2] * (x_aux[i] * x_aux[i])
    
    plt.plot(x, y, 'o', color='black')
    plt.plot(x_aux, y_aux, color='red')
    plt.show()

    return results

def reg_multipla(x1, x2, y):
    n = len(x)
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

    a = gauss_seidel(A, C, [0, 0, 0], 2e-4, showResult = False)

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

def gauss_seidel(A, c, x, tolerancia, showResult = True):
    # Ax = c

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

    mr = 1

    # Iterando
    while mr >= tolerancia:
        x_anterior = np.copy(x) # Vetor x da iteração anterior

        # Nova estimação de x: x = Cx + g
        for i in range(nl):
            x[i] = np.dot(C[i], x) + g[i]

        # Cálculo vetor m
        m = abs(x - x_anterior)
        #print(m)
        # Calculo de erro
        mr = max(m) / max(x)
        
        k+=1 # Incrementando contador

    if (showResult):
        print("Número de iterações =", k)
        #Printa o vetor x
        for i in range(nl):
            print(("x" + str(i + 1) + " ≈"), x[i])

    return x

x = [  0,   2,   4,  6,  8]
y = [110, 123, 119, 86, 62]

#ex_x = [1.5,  3, 4.5,   6,  7.5,   9,  10.5,   12]
#ex_y = [ 87, 74,  62,  59,   65,   71,   82,   94]

x1_m = [1250, 1300, 1350, 1250, 1300, 1250, 1300, 1350, 1350]
x2_m = [   6,    7,    6,    7,    6,    8,    8,    7,    8]
y_m =  [   8,   95,  101,   85,   92,   87,   96,  106,  108]

ex_x1 = [0,  2, 2.5, 1, 4,  7]
ex_x2 = [0,  1,   2, 3, 6,  2]
ex_y =  [5, 10,   9, 0, 3, 27]

reg_polinomial(x, y)
#reg_multipla(ex_x1, ex_x2, ex_y)
#reg_multipla(x1_m, x2_m, y_m)