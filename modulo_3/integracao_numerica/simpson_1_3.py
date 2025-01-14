import math
import numpy as np

"""
Diogo Nunes Batista

Trabalho 18
Integração númerica usando a regra 1/3 de Simpson
"""

def integral_simpson_1_3(f, a, b, n):
    """
    Calcula a integral definida usando a regra 1/3 de Simpson
    """

    x = np.linspace(a, b, n + 1)
    sum_impar = 0
    for i in range(1, n, 2): sum_impar+= f(x[i])
    sum_par = 0
    for i in range(2, n-1, 2): sum_par+= f(x[i])
    I = (b - a) * (f(x[0]) + 4 * sum_impar + + 2 * sum_par + f(x[n])) / (3 * n)
    return I

f = lambda x: math.log(x - 5, 3) # f(x)
a = 7 # Limite inferior
b = 17 # Limite superior
n = 20 # Número de intervalos

I = integral_simpson_1_3(f, a, b, n)
print(f"{I=}")