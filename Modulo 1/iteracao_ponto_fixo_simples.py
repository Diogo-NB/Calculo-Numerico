# -*- coding: utf-8 -*-
"""
@author: Diogo Nunes Batista

Estimação de raízes pelo método da Iteração de ponto fixo simples.
"""

def g(x): return (x**5/3 + x + 1)**(1/4)

xr1 = 2 # Estimativa inicial
xr2 = g(xr1) # Próxima estimativa

erro = 1e-4

while abs((xr2 - xr1)/xr2)*100 >= erro:
    xr1 = xr2
    xr2 = g(xr1) # Próxima estimativa
    
print("Raiz estimada = ",xr2)

