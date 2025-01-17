# Retorna um novo x4
from matplotlib import pyplot as plt
import numpy as np


def nova_estimativa(func ,x1, x2, x3):
    aux = (x2 - x1)*(func(x2) - func(x3))
    aux2 = (x2 - x3)*(func(x2) - func(x1))
    return x2 - (1/2) * ((aux*(x2 - x1)) - aux2*(x2 - x3)) / (aux - aux2)

# Retorna o ponto máximo considerando uma função "f" f(x)
# no intervalo determinado por três pontos (x1, x2, x3)
def interpolacao_quadratica(f, x1, x2, x3, erroMin = 1e-8):
    x4 = nova_estimativa(f ,x1, x2, x3)

    erro = 1

    if f(x2) > f(x4): xot = x2
    else: xot = x4
    i = 0

    while erro > erroMin:
        i+=1
        xot_anterior = xot

        if x4 > x2:
            if f(x4) > f(x2):
                x1 = x2
                x2 = x4
            else:
                x3 = x4
        else:
            if f(x4) > f(x2):
                x3 = x2
                x2 = x4
            else:
                x1 = x4
                
        x4 = nova_estimativa(f, x1, x2, x3)

        if f(x4) > f(x2): xot = x4
        else: xot = x2

        if i > 1:
            erro = abs((xot - xot_anterior) / xot)

    pMax = (xot,f(xot))
    print("Ponto máximo estimado = ", pMax)
    return pMax

# Retorna o ponto mínimo considerando uma função "f" f(x)
# no intervalo determinado por três pontos (x1, x2, x3)
def interpolacao_quadratica_min(f, x1, x2, x3, erroMin = 1e-8):
    x4 = nova_estimativa(f, x1, x2, x3)

    erro = 1

    if f(x2) < f(x4): xot = x2
    else: xot = x4
    i = 0

    while erro > erroMin:
        i+=1
        xot_anterior = xot

        if x4 > x2:
            if f(x4) < f(x2):
                x1 = x2
                x2 = x4
            else:
                x3 = x4
        else:
            if f(x4) < f(x2):
                x3 = x2
                x2 = x4
            else:
                x1 = x4
                
        x4 = nova_estimativa(f, x1, x2, x3)

        if f(x4) < f(x2): xot = x4
        else: xot = x2

        if i > 1:
            erro = abs((xot - xot_anterior) / xot)

    pMin = (xot,f(xot))
    print("Ponto máximo estimado = ", pMin)
    return pMin

def f(x): return (2*x) / (4 + 0.8 * x + x*x + 0.2 * (x**3))

# Intervalo
x1 = 0.5
x2 = 1
x3 = 3
k = (6+2+8)

x,y =interpolacao_quadratica(f, x1, x2, x3, erroMin=k*0.0001)

print('x =',round(x, 5))

# Vetores de auxilio para melhor visualização
l = 100 # Tamanho do vetor linspace
x_aux = np.linspace(0, 4 , l).astype(float)
y_aux = np.zeros(l)

for i in range(l):
    y_aux[i] = f(x_aux[i])

plt.plot(x, y, 'o', color='black')
plt.plot(x_aux, y_aux, color='red')
plt.show()