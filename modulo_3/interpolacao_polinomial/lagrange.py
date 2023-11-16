import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 3 - Trabalho 15

"""

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
        print(self.estimar(t))

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

x = [24, 25, 26, 27]
y = [89, 124, 154, 165]
t = 25.8
x == [25, 26, 27]

interpolador = InterpoladorLagrange(x, y)
interpolador.estimar_print(t)

from scipy.interpolate import lagrange

intp = lagrange(x, y)
print(intp)