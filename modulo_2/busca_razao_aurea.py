import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 6

"""

# Retorna o ponto máximo considerando uma função "func" f(x)
# no intervalo [x1, x2]
def busca_razao_aurea(func, x1, x2, erroMin = 1e-8):

    # Constante - Razão áurea
    phi = (1 + np.sqrt(5)) / 2

    # intervalo de busca inicial
    xu = x1
    xl = x2
    xot = x2

    erro = 1

    # Iterando
    while erro >= erroMin:
        d = (phi - 1)*(xu - xl)
        x1 = xl + d
        x2 = xu - d

        # Determinando qual intervalo possui o valor máximo
        # e reajustando o novo intervalo de acordo
        if func(x1) > func(x2):
            xot = x1
            xl = x2
        else:
            xot = x2
            xu = x1

        # Cálculo do erro
        erro = (2 - phi)*abs((xu - xl)/xot)*100

    # Ponto máximo
    pMax = (xot, func(xot))

    print("Ponto máximo estimado = ", pMax)
 
    return pMax

# Retorna o ponto mínimo considerando uma função "func" f(x)
# no intervalo [x1, x2]
def busca_razao_aurea_min(func, x1, x2, erroMin = 1e-8):

    # Constante - Razão áurea
    phi = (1 + np.sqrt(5)) / 2

    # intervalo de busca inicial
    xu = x1
    xl = x2
    xot = x2

    erro = 1
   
    # Iterando
    while erro >= erroMin:
        d = (phi - 1)*(xu - xl)
        x1 = xl + d
        x2 = xu - d

        # Determinando qual intervalo possui o valor máximo
        # e reajustando o novo intervalo de acordo
        if func(x1) < func(x2):
            xot = x1
            xl = x2
        else:
            xot = x2
            xu = x1

        # Cálculo do erro
        erro = (2 - phi)*abs((xu - xl)/xot)*100

    # Ponto máximo
    pMin = (xot, func(xot))

    print("Ponto mínimo estimado = ", pMin)

    return pMin

def func(x): return (x**5)/3 - x**4 + x + 1

# Intervalo
x1 = -1
x2 = 1.5

busca_razao_aurea(func, x1, x2)