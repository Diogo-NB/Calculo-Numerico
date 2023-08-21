# -*- coding: utf-8 -*-

"""
@author: Diogo Nunes Batista

Estimação de raízes pelo método da secante modificado.
"""

def f(x): return (x**5)/3 - x**4 + x + 1

ptb = 1e-6 # Pertubação
erro = 1e-4
xr1 = 2 # Estimativa inicial
xr2 = xr1 - (ptb*xr1*f(xr1))/(f(xr1 + ptb*xr1) - f(xr1))  # Próxima estimativa

while abs((xr2 - xr1)/xr2)*100 >= erro:
    xr1 = xr2
    xr2 = xr1 - (ptb*xr1*f(xr1))/(f(xr1 + ptb*xr1) - f(xr1))  # Próxima estimativa
    
print("Raiz estimada = ",xr2)

