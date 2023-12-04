import numpy as np

"""
Diogo Nunes Batista

Trabalho 22
Solução de Equações Diferenciais Ordinárias usando o método de Heun com iteração
"""

def metodoHeunIterativo(f, a, b, f0, h, erroMin = 0, n_iteracoes = np.inf):
    # Cria um vetor que vai de a até b com espaço
    # de 'h' entre cada elemento
    t = np.arange(a, b + h, h)
    n = len(t)
    y = np.zeros(n)
    y[0] = f0 # Atribuindo a condição inicial à y[0]

    for i in range(n-1):
        # Resultado de f(ti, yi)
        f_ty = f(t[i], y[i])
        # Equação preditora
        y[i+1] = y[i] + f_ty*h
        erro = np.inf
        # Iteracao da equação corretora
        cont = 0 # Contador da iteracao
        while erro > erroMin and cont < n_iteracoes:
            # Resultado y[i+1] da iteracao anterior
            y_anterior = y[i+1]
            # Equação corretora
            y[i+1] = y[i] + (f_ty + f(t[i+1], y[i+1])) * h / 2
             # Cálculo do erro
            erro = abs((y[i+1] - y_anterior) / y[i+1]) * 100
            cont+=1  

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

y = metodoHeunIterativo(f, a, b, f0, h, n_iteracoes=5)
print(f"y = {y}")