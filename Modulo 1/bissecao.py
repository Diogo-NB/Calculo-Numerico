# -*- coding: utf-8 -*-
import numpy as np
"""
@author: Diogo Nunes Batista

Estimação de raízes pelo método da bisseção
"""

# Declaração da função
def func(x): return 2*np.log(x-1) + 3

a = 1.002
b = 2
# Ponto médio (xo)
xo = (a + b) / 2
erro = np.inf
count = 0

while erro >= 0.00001:
    Yo = func(xo) #f(xo)

    if func(a)*Yo < 0:
        b = xo
    elif Yo*func(b) < 0:
        a = xo
        
    xo_anterior = xo
    xo = (a + b) / 2
        
    erro = abs((xo - xo_anterior)/xo)

print("Raiz estimada = ",xo)


    

    
     

    


