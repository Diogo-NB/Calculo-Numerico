# -*- coding: utf-8 -*-

"""
@author: Diogo Nunes Batista

Módulo 1 - Trabalho 5
Estimação de raízes pelo método da secante modificado.
"""

def f(x): return (x**5)/3 - x**4 + x + 1

ptb = 1e-6 # Pertubação
erroMin = 1e-4 # Condição de parada, mínimo de erro aceito 
xr1 = 2 # Estimativa inicial
xr2 = xr1 - (ptb*xr1*f(xr1))/(f(xr1 + ptb*xr1) - f(xr1))  # Próxima estimativa

# Enquanto não achar uma estimativa com nível aceitável de erro
while abs((xr2 - xr1)/xr2)*100 >= erroMin:
    xr1 = xr2
    xr2 = xr1 - (ptb*xr1*f(xr1))/(f(xr1 + ptb*xr1) - f(xr1))  # Próxima estimativa
    
print("Raiz estimada = ",xr2)

