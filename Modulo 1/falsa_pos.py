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
    # Definindo o próximo subintervalo
    if func(xr) == 0:
        break
    elif func(xl)*func(xr) < 0:
        xu = xr
    elif func(xr)*func(xu) < 0:
        xl = xr
        
    xr_anterior = xr
    # Nova estimativa de raíz
    xr = xu - (func(xu)*(xl - xu))/(func(xl) - func(xu))
        
    # Cálculo do novo erro
    erro = abs((xr - xr_anterior)/xr)

print("Raiz estimada = ", xr)


    

    
     

    


