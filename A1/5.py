import matplotlib.pyplot as plt
import numpy as np

# Retorna os parâmetros calculados e o coeficiente de determinação de uma regressão linear 
def reg_linear(x, y):
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
    
    print("Coeficientes do modelo linear: y = a1x + a0")
    print(results)

    novo_y = np.zeros(n)

    for i in range(n):
        novo_y[i] = a1*x[i] + a0

    plt.plot(x, y, 'o', color='black')
    plt.plot(x, novo_y, color='red')
    plt.show()

    return results

k = [6, 2, 8]

x = [-50, -30, 0, 60, 90, 110]
y = [1250+k[0], 1280+k[2], 1350+k[1], 1480+k[0], 1580+k[2], 1700+k[1]]

res = reg_linear(x, y)

print('a1 =', round(res['a1'],5))
print('a0 =', round(res['a0'],5))
print('r² =', round(res['r²'],5))