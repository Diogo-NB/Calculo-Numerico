import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 3 - Trabalho 15
Polinômio interpolador de Lagrange
"""

def intervaloMaisProximo(tamanho, array, pivot):
    """
    Retorna um sub-array de array de tamanho 'tamanho' em que resulta na menor distância total de seus elementos até 'pivot'
    """
    n = len(array)
    if n < tamanho:
        return
    elif n == tamanho:
        return array

    i = 0
    j = n - 1

    for k in range(n - tamanho):
        if array[j] - pivot > pivot - array[i]:
            j-=1
        else:
            i+=1
       
    intervalo = np.zeros(tamanho)

    for k in range(i, j + 1):
        intervalo[k - i] = array[k]

    return intervalo

class InterpoladorLagrange:
    """
    Uma classe de implementação de interpolação usando o método de Lagrange
    """

    def __init__(self, x, y):
        """
        Construtor 

        Parâmetros:
        - x: vetor x
        - y: vetor f(x)
        """

        self.n = len(x) # Tamanho de x

        if self.n != len(y):
            raise ValueError("Tamanho de x e y devem ser iguais!")

        self.x = np.array(x)
        self.y = np.array(y)  

    def estimar(self, t):
        """
        Estima f(t) utilizando o método de interpolação de Lagrange

        Parâmetros:
        - t: o valor para qual a estimativa será calculada

        Retorna:
        - A estimativa de f(t)
        """
        res = 0
        for i in range(self.n):
            # Variavel auxiliar para o cálculo de Li
            aux = 1
            for j in range(self.n):
                if i != j:
                    aux *= (t - self.x[j]) / (self.x[i] - self.x[j])
            #     Li  *   f(xi)
            res+= aux * self.y[i]
        return res

# Trabalho 15
x = [25, 26, 27]
y = [124, 154, 165]
t = 25.8

# Criando o objeto InterpoladorLagrange com base nos vetores x e y
interpoladorLagrange = InterpoladorLagrange(x, y)

# Estima o valor de t e printa na tela
result = interpoladorLagrange.estimar(t)
print(f"f({t}) = {result}")