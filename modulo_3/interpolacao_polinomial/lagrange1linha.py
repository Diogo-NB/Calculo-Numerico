import numpy as np
from time import perf_counter

"""
@author: Diogo Nunes Batista
Polinômio interpolador de Lagrange usando apenas uma linha de código
"""

# Retorna a estimação de f(t)
def metodoLagrange(x, y, t): return np.sum([(np.prod([np.prod([(t - xj) / (x[i] - xj) for xj in x[:i]]), np.prod([(t - xj) / (x[i] - xj) for xj in x[i+1:]])]) * (y[i])) for i in range(len(x))])

# Trabalho 15
x = [25, 26, 27]
y = [124, 154, 165]
t = 25.8

t1_start = perf_counter()
print(f"f({t}) = {metodoLagrange(x, y, t)}")
t1_stop = perf_counter()
 
print("Time:", t1_stop-t1_start)