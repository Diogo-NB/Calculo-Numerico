# -*- coding: utf-8 -*-
import numpy as np
"""
@author: Diogo Nunes Batista

Módulo 1 - Trabalho 3
Estimação de raízes pelo método da falsa posição
"""

# Declaração da função
def func(x): return 2*np.log(x-1) + 3

# Variáveis que delimitam o intervalo
xl = 1.002 
xu = 2.000 

# Raíz estimada
xr = xu - (func(xu)*(xl - xu))/(func(xl)-func(xu))

erro = np.inf
erroMin = 0.00001 # Condição de parada, mínimo de erro aceito

# Enquanto não achar o subintervalo que possui a raíz ao nível aceito de erro
while erro >= erroMin:
    Yl = func(xl) #f(xl))
    Yu = func(xu) #f(xu)
    Yr = func(xr) #f(xr)

    # Definindo o próximo subintervalo
    if Yl*Yr < 0:
        xu = xr
    elif Yr*Yu < 0:
        xl = xr
        
    xr_anterior = xr
    # Nova estimativa de raíz
    xr = xu - (Yu*(xl - xu))/(Yl - Yu)
        
    # Cálculo do novo erro
    erro = abs((xr - xr_anterior)/xr)

print("Raiz estimada = ", xr)


    

    
     

    


