# -*- coding: utf-8 -*-
import numpy as np
"""
@author: Diogo Nunes Batista

Estimação de raízes pelo método da falsa posição
"""

# Declaração da função
def func(x): return 2*np.log(x-1) + 3

xl = 1.002 
xu = 2.000 
# Ponto médio
xr = xu - (func(xu)*(xl - xu))/(func(xl)-func(xu))

erro = np.inf
count = 0

while erro >= 0.00001:
    Yl = func(xl) #f(xl))
    Yu = func(xu) #f(xu)
    Yr = func(xr) #f(xr)

    if Yl*Yr < 0:
        xu = xr
    elif Yr*Yu < 0:
        xl = xr
        
    xr_anterior = xr
    xr = xu - (Yu*(xl - xu))/(Yl - Yu)
        
    erro = abs((xr - xr_anterior)/xr)

print("Raiz estimada = ",xr)


    

    
     

    


