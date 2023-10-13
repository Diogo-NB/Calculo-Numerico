# -*- coding: utf-8 -*-
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 7

"""
def f(x): return (x**5)/3 - x**4 + x + 1

def nova_estimativa(x1, x2, x3):
    aux = (x2 - x1)*(f(x2) - f(x3))
    aux2 = (x2 - x3)*(f(x2) - f(x1))
    return x2 - (1/2) * ((aux*(x2 - x1)) - aux2*(x2 - x3)) / (aux - aux2)

x1 = -1
x2 = 0
x3 = 1
x4 = nova_estimativa(x1, x2, x3)

erroMin = 1e-8
erro = 1

if f(x2) > f(x4): xot = x2
else: xot = x4
i = 0

while erro > erroMin:
    i+=1
    xot_anterior = xot

    if x4 > x2:
        if f(x4) > f(x2):
            x1 = x2
            x2 = x4
        else:
            x3 = x4
    else:
        if f(x4) > f(x2):
            x3 = x2
            x2 = x4
        else:
            x1 = x4
            
    x4 = nova_estimativa(x1, x2, x3)

    if f(x4) > f(x2): xot = x4
    else: xot = x2

    if i > 1:
        erro = abs((xot - xot_anterior) / xot)

print("Ponto máximo estimado = ", [xot,f(xot)])

    

