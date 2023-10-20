k = (6 + 2 + 8) / 27

def f(x): return 1 - 5*k*x + x**3

ptb = 1e-2 # Pertubação
erroMin = 0.0001 # Condição de parada, mínimo de erro aceito 
xr1 = 0.2 # Estimativa inicial
xr2 = xr1 - (ptb*xr1*f(xr1))/(f(xr1 + ptb*xr1) - f(xr1))  # Próxima estimativa

# Enquanto não achar uma estimativa com nível aceitável de erro
while abs((xr2 - xr1)/xr2)*100 > erroMin:
    xr1 = xr2
    xr2 = xr1 - (ptb*xr1*f(xr1))/(f(xr1 + ptb*xr1) - f(xr1))  # Próxima estimativa
    
print("Raiz estimada = ", round(xr2, 5))
print('f(raiz) =', round(f(xr2), 5))

