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

    def estimar_print(self, t):
        result = self.estimar(t)
        print(f"f({t}) = {result}")    

    def estimar(self, t):
        return self.__f(t)

    def __f(self, t):
        res = 0
        for i in range(self.n):
            res+= (self.__L(i, t)) * (self.y[i])
        return res

    def __L(self, i, t):
        res = 1
        for j in range(self.n):
            if i != j:
                res *= (t - self.x[j]) / (self.x[i] - self.x[j])
        return res

# Trabalho 15
x = [25, 26, 27]
y = [124, 154, 165]
t = 25.8

# Criando o objeto InterpoladorLagrange com base nos vetores x e y
interpoladorLagrange = InterpoladorLagrange(x, y)

# Estima o valor de t e printa na tela
interpoladorLagrange.estimar_print(t)