import numpy as np
from time import perf_counter

"""
Implementação metodo de lagrange com apenas uma linha de codigo
SIM, vc leu corretamente
"""

# Retorna a estimação de f(t)
def metodoLagrange(x, y, t): return np.sum([(np.prod([np.prod([(t - xj) / (x[i] - xj) for xj in x[:i]]), np.prod([(t - xj) / (x[i] - xj) for xj in x[i+1:]])]) * (y[i])) for i in range(len(x))])

x = np.linspace(0, 10, 1000)
y = np.sin(x)
t = 5
t1_start = perf_counter()
print(f"f({t}) = {metodoLagrange(x, y, t)} e sin({t}) = {np.sin(t)}")
t1_stop = perf_counter()
 
print("Time:", t1_stop-t1_start)