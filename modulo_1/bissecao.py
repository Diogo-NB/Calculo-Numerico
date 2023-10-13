# -*- coding: utf-8 -*-
import numpy as np
"""
@author: Diogo Nunes Batista
Módulo 1 - Trabalho 2

Estimação de raízes pelo método da bisseção
"""

# Declaração da função
def func(x): return 2*np.log(x-1) + 3

a = 1.002
b = 2
# Ponto médio (xo)
xo = (a + b) / 2
erro = np.inf
erroMin = 0.00001 # Condição de parada, mínimo de erro aceito

# Enquanto não achar o subintervalo que possui a raíz ao nível aceito de erro
while erro >= erroMin: 
    Yo = func(xo) #f(xo)

    # Definindo o próximo subintervalo
    if func(a)*Yo < 0:
        b = xo 
    elif Yo*func(b) < 0:
        a = xo 
        
    xo_anterior = xo

    # Novo ponto médio
    xo = (a + b) / 2
        
    # Cálculo do novo erro
    erro = abs((xo - xo_anterior)/xo)

print("Raiz estimada = ",xo)


    

    
     

    


