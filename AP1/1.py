import numpy as np

k = (6 + 2 + 8) / 27

# Declaração da função
def func(x): return 1 - 3 * k * x + x**3

# Variáveis que delimitam o intervalo
xl = -2 
xu = -1 

# Raíz estimada
xr = xu - (func(xu)*(xl - xu))/(func(xl)-func(xu))

erro = np.inf
erroMin = 0.0005 # Condição de parada, mínimo de erro aceito

# Enquanto não achar o subintervalo que possui a raíz ao nível aceito de erro
while erro > erroMin:
    # Definindo o próximo subintervalo
    if func(xr) == 0:
        break
    elif func(xl)*func(xr) < 0:
        xu = xr
    elif func(xr)*func(xu) < 0:
        xl = xr
        
    xr_anterior = xr
    # Nova estimativa de raíz
    xr = xu - (func(xu)*(xl - xu))/(func(xl) - func(xu))
        
    # Cálculo do novo erro
    erro = abs((xr - xr_anterior)/xr)

print("Raiz estimada = ", round(xr, 5))

print('f(raiz) =', round(func(xr), 5))