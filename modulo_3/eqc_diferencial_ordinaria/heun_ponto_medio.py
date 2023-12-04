import numpy as np

"""
Diogo Nunes Batista

Trabalho 23
Solução de Equações Diferenciais Ordinárias usando o método do ponto médio
"""

def metodoPontoMedio(f, a, b, f0, h):
    # Cria um vetor que vai de a até b com espaço
    # de 'h' entre cada elemento
    t = np.arange(a, b + h, h)
    n = len(t)
    y = np.zeros(n)
    y[0] = f0 # Atribuindo a condição inicial à y[0]

    for i in range(0, n-1):
        # Equação preditora
        y_med = y[i] + f(t[i], y[i])*h / 2 # y[i+1/2]
        # Equação corretora
        y[i+1] = y[i] + f((t[i] + t[i+1]) / 2, y_med) * h

    return y

"""
#Exemplo do slide
f = lambda t, y: 4 * np.e ** (0.8 * t) - 0.5 * y
f0 = 2 # Condição inicial, f(t[0])

# Intervalo
a = 0
b = 4
# passo
h = 1
"""
f = lambda x, y: -2*y + 4 * np.e ** (-x)
f0 = 2 # Condição inicial, f(t[0])

# Intervalo
a = 0
b = 1
# passo
h = 0.2

y = metodoPontoMedio(f, a, b, f0, h)
print(f"y = {y}")