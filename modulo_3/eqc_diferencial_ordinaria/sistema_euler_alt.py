import numpy as np

"""
Diogo Nunes Batista

Solução de Sistemas de Equações Diferenciais Ordinárias usando o método de Euler
"""

# Equações diferenciais do sistema, y = y1 ; z = y2
dy1dx = lambda x, y, z: -2 * y + 4 * np.e ** (-x)
dy2dx = lambda x, y, z: -y*z*z / 3

# Intervalo
a = 0
b = 1

# Passo
h = 0.2

# Cria um vetor que vai de a até b com espaço
# de 'h' entre cada elemento
t = np.arange(a, b + h, h)
n = len(t)

# Vetores solução do sistema
y1 = np.zeros(n) # y
y2 = np.zeros(n) # z

# Condições iniciais do sistema, y(0) = y1[0] ; z(0) = y2[0]
y1[0] = 2
y2[0] = 4

for i in range(0, n-1):
    y1[i+1] = y1[i] + dy1dx(t[i], y1[i], y2[i])*h
    y2[i+1] = y2[i] + dy2dx(t[i], y1[i], y2[i])*h

print(f"y = {y1}\nz = {y2}")




