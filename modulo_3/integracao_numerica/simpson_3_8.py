import math
import numpy as np
from scipy.integrate import quad as integral_scipy

"""
Diogo Nunes Batista

Trabalho 19
Integração númerica usando a regra 3/8 de Simpson
"""

def integral_simpson_3_8(f, a, b, n):
    """
    Calcula a integral definida usando a regra 3/8 de simpson
    """

    x = np.linspace(a, b, n + 1)
    sum = 0
    for i in range(1, n): sum+= f(x[i])
    sum_multiplo_3 = 0
    for i in range(3, n, 3): sum_multiplo_3+= f(x[i])

    I = 3* (b - a) * (f(x[0]) + 3 * (sum - sum_multiplo_3) + + 2 * sum_multiplo_3 + f(x[n])) / (8 * n)
    return I

'''
def f(x): return 0.2 + 25*x - 200 * (x**2) + 675 * (x**3) - 900 * (x**4) + 400 * (x**5) # Exemplo do slide

a = 0
b = 0.8
n = 4

'''

f = lambda x: math.log(x - 5, 3) # f(x)
a = 7 # Limite inferior
b = 17 # Limite superior
n = 20 # Número de intervalos

I = integral_simpson_3_8(f, a, b, n)
print(f"{I=}")

# Cálculo da integral usando o scipy, a fim de teste
print(f"{integral_scipy(f, a, b)=}")