# -*- coding: utf-8 -*-
"""
@author: Diogo Nunes Batista

Módulo 1 - Trabalho 4
Estimação de raízes pelo método da Iteração de ponto fixo simples.
"""

def g(x): return (x**5/3 + x + 1)**(1/4)

xr1 = 2 # Estimativa inicial
xr2 = g(xr1) # Próxima estimativa

erroMin = 1e-5 # Condição de parada, mínimo de erro aceito

# Enquanto não achar uma estimativa com nível aceitável de erro
while abs((xr2 - xr1)/xr2)*100 > erroMin:
    xr1 = xr2
    xr2 = g(xr1) # Próxima estimativa
    
print("Raiz estimada = ",xr2)

