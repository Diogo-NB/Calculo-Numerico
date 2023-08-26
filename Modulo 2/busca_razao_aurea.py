# -*- coding: utf-8 -*-
import numpy as np
"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 6

"""
def func(x): return (x**5)/3 - x**4 + x + 1

phi = (1 + np.sqrt(5)) / 2
erroMin = 1e-8

# intervalo de busca inicial
xu = -1
xl = 1.5
xot = 1.5

while (2 - phi)*abs((xu - xl)/xot)*100 >= erroMin:
    d = (phi - 1)*(xu - xl)
    x1 = xl + d
    x2 = xu - d
    if func(x1) > func(x2):
        xot = x1
        xl = x2
    else:
        xot = x2
        xu = x1

print("Ponto máximo estimado = ", [xot,func(xot)])