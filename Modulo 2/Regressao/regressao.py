#%%
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def reg_linear(x, y, showResults = True, ylabel = None, xlabel = None):
    # y = a1x + a0
    x = np.array(x, dtype="float64")
    y = np.array(y, dtype="float64")

    n = x.shape[0]

    Sx = 0
    Sy = 0
    Sxy = 0
    Sx2 = 0
    Sy2 = 0

    # Calculando as somas
    for i in range(n):
        Sx += x[i]
        Sy += y[i]
        Sxy += x[i] * y[i]
        Sx2 += x[i] * x[i]
        Sy2 += y[i] * y[i]

    # médias
    avg_x = Sx / n
    avg_y = Sy / n

    # Cálculo de a1 e a0
    a1 = (n*Sxy - Sx*Sy ) / (n*Sx2 - Sx*Sx)
    a0 = avg_y - a1*avg_x

    # Soma dos quadrados dos resíduos estimados
    Sr = 0
    # Soma total dos quadrados em torno da média da variável dependente y é dada por
    St = 0

    for i in range(n):
        e = y[i] - a0 - a1*(x[i])
        Sr += e*e
        St += (y[i] - avg_y) * (y[i] - avg_y)

    # Coeficiente de Determinação
    r2 = (St - Sr) / St

    results = {
        "a1": a1,
        "a0" : a0,
        "r²" : r2
        }
    
    if showResults:
        print(results)

        novo_y = np.zeros(n)

        for i in range(n):
            novo_y[i] = a1*x[i] + a0

        plt.plot(x, y, 'o', color='black')
        plt.plot(x, novo_y, color='red')
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.show()

    return results

def reg_exponencial(x, y, ylabel = None, xlabel = None):
    # y = a * e^(bx) 
    
    # Linearizando
    x_linear = np.array(x, dtype="float64")
    y_linear = np.log(y)

    # Tamanho de x e y
    n = x_linear.shape[0]

    results = reg_linear(x_linear, y_linear, showResults= True)

    # Calculando os parametros para a função original
    a = np.e ** (results['a0'])
    b = results['a1']

    # Soma dos quadrados dos resíduos estimados
    Sr = 0
    # Soma total dos quadrados em torno da média da variável dependente y
    St = 0
    # Média de y
    avg_y = np.average(y)

    for i in range(n):
        # y = a * e^(bx)
        e = y[i] - a * np.e ** (b*x[i])
        Sr += e*e
        St += (y[i] - avg_y) * (y[i] - avg_y)

    # Coeficiente de Determinação
    r2 = (St - Sr) / St
    
    # Novo resultado com os corretos parametros
    results = {
        'a': a,
        'b': b,
        'r²': r2
        }
    
    print(results)

    y_calculado = np.zeros(n)
    
    for i in range(n):
        y_calculado[i] = a * (np.e ** (b*x[i]))

    plt.plot(x, y, 'o', color='black')
    plt.plot(x, y_calculado, color='red')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()

def reg_potencia(x, y, ylabel = None, xlabel = None):
    # y = a * x^b 
    
    # Linearizando
    x_linear = np.log10(x)
    y_linear = np.log10(y)

    # Tamanho de x e y
    n = x_linear.shape[0]

    results = reg_linear(x_linear, y_linear, showResults= True)

    # Calculando os parametros para a função original
    a = 10 ** (results['a0'])
    b = results['a1']

    # Soma dos quadrados dos resíduos estimados
    Sr = 0
    # Soma total dos quadrados em torno da média da variável dependente y
    St = 0
    # Média de y
    avg_y = np.average(y)

    for i in range(n):
        e = y[i] - a * (x[i]) ** b
        Sr += e*e
        St += (y[i] - avg_y) * (y[i] - avg_y)

    # Coeficiente de Determinação
    r2 = (St - Sr) / St
    
    # Novo resultado com os corretos parametros
    results = {
        'a': a,
        'b': b,
        'r²': r2
        }
    
    print(results)

    y_calculado = np.zeros(n)
    
    for i in range(n):
        y_calculado[i] = a * (x[i]) ** b

    plt.plot(x, y, 'o', color='black')
    plt.plot(x, y_calculado, color='red')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
    
x = [4.3, 4.5, 5.9, 5.6, 6.1, 5.2, 3.8, 2.1, 7.5]
y = [126, 121, 116, 118, 114, 118, 132, 141, 108]

ex_x = [10, 20, 30,   40,  50,   60,  70,   80]
ex_y = [25, 70, 380, 550, 610, 1220, 830, 1450]

reg_exponencial(ex_x, ex_y)