import numpy as np
from numpy.linalg import norm as mod
"""
@author: Diogo Nunes Batista
Módulo 3 - Trabalho 14

"""

def intervaloMaisProximo(intervalSize, array, pivot):
    n = len(array)
    if n < intervalSize:
        return
    elif n == intervalSize:
        return array

    i = 0
    j = n - 1

    for k in range(n - intervalSize):
        if x[j] - pivot > pivot - x[i]:
            j-=1
        else:
            i+=1
       
    intervalo = np.zeros(intervalSize)

    for k in range(i, j + 1):
        intervalo[k - i] = x[k]

    return intervalo

# Polinômio interpolador de 3ª ordem
ordem = 3

#x = [24,  25,  26,  27,  28,  29]
# f(x)
#y = [89, 124, 154, 165, 179, 194]

x = [4, 1, 5, 6]
y = [np.log(4), 0, np.log(5), np.log(6)]
est = 2

x = np.array(x)
y = np.array(y)

x = intervaloMaisProximo(ordem + 1, x, est)
n = len(x)
b = list()

def f(x, y, i, j):
    if i == j:
        res = y[i]
        if i == 0:
            b.append(res)

        #print(i, ': T =', (x[i], y[i]))
        print("f( x", i+1, " ) = ", res, sep='')
        return res
    
    res = ( - f(x, y, i, j - 1) + f(x, y, i + 1, j) ) / ( + x[j] - x[i])
    print("f( ", end='', sep='')
    for k in range(i+1, j+2):
        print("x", k, end=' ', sep='')
    print(") = ", res)

    if i == 0:
        b.append(res)

    return res

print( f(x, y, 0, n - 1) )

f_est = b[0]
for i in range(1, len(b)):
    aux = b[i]
    for j in range(i):
        aux*=(est - x[j])
    f_est+=aux

print('f(', est ,')≈', f_est, sep= '')

