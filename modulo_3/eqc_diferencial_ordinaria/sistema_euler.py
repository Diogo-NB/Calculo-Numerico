import numpy as np

"""
Diogo Nunes Batista

Trabalho 20
"""

def metodoSitemaEuler(sis, a, b, condIni, h):
    # Cria um vetor que vai de a até b com espaço
    # de 'h' entre cada elemento
    qtdEDO = len(sis)
    # Checando se há condições inicais para cada EDO
    if (qtdEDO > len(condIni)):
        raise Exception("Não há condições iniciais suficiente")
    
    t = np.arange(a, b + h, h)
    n = len(t)
    # Criando uma matriz para armazenar o resultado de cada solução para as EDOs
    matriz_solucoes_y = np.zeros((qtdEDO, n))

    matriz_solucoes_y[:, 0] = condIni

    # A primeira função do sistema recebe apenas y1 como parâmetro
    # A segunda função do sistema recebe y1 e y2 como parâmetro
    # A n-ésima função do sitema recebe y1, y2 ... yn como parâmetro
    # Assim é necessário armazenar (em aux) os valores intermediarios
    # de y1, y2 ... yn até a iteração atual

    aux = np.zeros(qtdEDO) # Vetor auxiliar

    # Para cada t, calcular y1, y2 ... yn
    for i in range(n-1):

        # Calculando y1, y2 ... yn de t[i]
        for j in range(qtdEDO):
            y = matriz_solucoes_y[j] # Vetor y dessa iteração
            f = sis[j] # Função f dessa iteração
            # Adicionando/atualizando o próximo valor para o vetor auxiliar
            aux[j] = y[i]
            y[i+1] = y[i] + f(t[i], aux)*h

    return matriz_solucoes_y

"""
#Exemplo do slide

# Vetor das EDOs, paramêtro y sendo o vetor que representa y1, y2 ... yn
sistema = [
        lambda x, y: -0.5*(y[0]),
        lambda x, y: 4 - 0.3*y[1] - 0.1*y[0]
          ]

condicoesIniciais = [4.0, 6.0] # Condição inicial, y1(t[0]), y2(t[0]) ... yn(t[n]) 

# Intervalo
a = 0
b = 2
# passo
h = 0.5

y1, y2 = metodoSitemaEuler(sistema, a, b, condicoesIniciais, h)
print(f"{y1=}\n{y2=}")
"""
# Vetor das EDOs, paramêtro y sendo o vetor que representa y1, y2 ... yn
sistema = [
        lambda x, y: -2*y[0] + 4 * np.e **(-x),
        lambda x, y: - y[0]*y[1]*y[1] / 3
          ]

condicoesIniciais = [2, 4] # Condição inicial, y1(t[0]), y2(t[0]) ... yn(t[n]) 

# Intervalo
a = 0
b = 1
# passo
h = 0.2

y1, y2 = metodoSitemaEuler(sistema, a, b, condicoesIniciais, h)
print(f"{y1=}\n{y2=}")