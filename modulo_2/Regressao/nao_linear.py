import matplotlib.pyplot as plt
import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 2 - Trabalho 11

"""

# Retorna os parâmetros calculados e o coeficiente de determinação de uma regressão linear 
def reg_linear(x, y, showResults = True, graphTitle = None):
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
        print("Coeficientes do modelo linear/linearizado: y = a1x + a0")
        print(results)

        novo_y = np.zeros(n)

        for i in range(n):
            novo_y[i] = a1*x[i] + a0

        plt.plot(x, y, 'o', color='black')
        plt.plot(x, novo_y, color='red')
        plt.title(graphTitle)
        plt.show()

    return results

# Regressão não-lineares

def reg_exponencial(x, y):
    # y = a * e^(bx) 
    
    # Linearizando
    x_linear = np.array(x, dtype="float64")
    y_linear = np.log(y)

    # Tamanho de x e y
    n = x_linear.shape[0]

    results = reg_linear(x_linear, y_linear, showResults= True, graphTitle="Regressão - Exponencial linearizada")

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
        e = y[i] - a * (np.e ** (b*x[i]))
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
    
    print("Coeficientes do modelo exponencial: y = a * e^(bx)")
    print(results)
    
    # Vetores de auxilio para melhor visualização
    l = 200 # Tamanho do vetor linspace
    x_aux = np.linspace(min(x), max(x) , l).astype(float)
    y_aux = np.zeros(l)

    for i in range(l):
        y_aux[i] = a * (np.e ** (b*x_aux[i]))
    
    plt.plot(x, y, 'o', color='black')
    plt.plot(x_aux, y_aux, color='red')
    plt.title("Regressão - Exponencial")
    plt.show()

    return results

def reg_potencia(x, y):
    # y = a * x^b 
    
    # Linearizando
    x_linear = np.log10(x)
    y_linear = np.log10(y)

    # Tamanho de x e y
    n = x_linear.shape[0]

    results = reg_linear(x_linear, y_linear, showResults= True, graphTitle="Regressão - Potencia linearizada")

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
    
    print("Coeficientes do modelo potência: y = a * x^b")
    print(results)
    
    # Vetores de auxilio para melhor visualização
    l = 200 # Tamanho do vetor linspace
    x_aux = np.linspace(min(x), max(x) , l).astype(float)
    y_aux = np.zeros(l)

    for i in range(l):
        y_aux[i] = a * (x_aux[i]) ** b
    
    plt.plot(x, y, 'o', color='black')
    plt.plot(x_aux, y_aux, color='red')
    plt.title("Regressão - Potencia")
    plt.show()
    
def reg_saturacao(x, y):
    # y = a * x / (b + x)
    
    # Linearizando
    x_linear = np.divide(1, x)
    y_linear = np.divide(1, y)

    # Tamanho de x e y
    n = x_linear.shape[0]

    results = reg_linear(x_linear, y_linear, showResults= True, graphTitle="Regressão - Saturação linearizada")

    # Calculando os parametros para a função original
    a = 1 / (results['a0'])
    b = a * (results['a1'])

    # Soma dos quadrados dos resíduos estimados
    Sr = 0
    # Soma total dos quadrados em torno da média da variável dependente y
    St = 0
    # Média de y
    avg_y = np.average(y)

    for i in range(n):
        e = y[i] - (a*(x[i])) / (b + x[i])
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
    
    print("Coeficientes do modelo saturação: y = a * e^(bx)")
    print(results)
    
    # Vetores de auxilio para melhor visualização
    l = 200 # Tamanho do vetor linspace
    x_aux = np.linspace(min(x), max(x) , l).astype(float)
    y_aux = np.zeros(l)

    for i in range(l):
        y_aux[i] = (a*(x_aux[i])) / (b + x_aux[i])
    
    plt.plot(x, y, 'o', color='black')
    plt.plot(x_aux, y_aux, color='red')
    plt.title("Regressão - Saturação")
    plt.show()

x = [4.3, 4.5, 5.9, 5.6, 6.1, 5.2, 3.8, 2.1, 7.5]
y = [126, 121, 116, 118, 114, 118, 132, 141, 108]

#ex_x = [10, 20, 30,   40,  50,   60,  70,   80]
#ex_y = [25, 70, 380, 550, 610, 1220, 830, 1450]

print("--------- Modelo Exponencial ---------")
reg_exponencial(x, y)

print("\n--------- Modelo Potencia ---------")
reg_potencia(x, y)

print("\n--------- Modelo Saturação ---------")
reg_saturacao(x, y)
