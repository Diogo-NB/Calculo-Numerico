import math
import numpy as np
import timeit

"""
Diogo Nunes Batista

Trabalho 17
"""

def integral_trapezoidal(f, a, b, n):
    """
    Calcula a integral definida usando a regra trapezoidal múltipla
    """
    x = np.linspace(a, b, n + 1)
    sum = np.sum(list(map(f, x[1:n])))

    I = (b - a) * (f(x[0]) + 2 * sum + f(x[n])) / (2 * n)
    return I

'''
def f_exemplo(x): return 0.2 + 25*x - 200 * (x**2) + 675 * (x**3) - 900 * (x**4) + 400 * (x**5)

a = 0
b = 0.8
n = 4

'''

f = lambda x: math.log(x - 5, 3) # f(x)
a = 7 # Limite inferior
b = 17 # Limite superior
n = 20 # Número de intervalos

resultado = integral_trapezoidal(f, a, b, n)
print(f"{resultado=}")