import numpy as np

"""
@author: Diogo Nunes Batista
Módulo 3 - Trabalho 16
Interpolação inversa com o interpolador de Newton e busca incremental
"""

class InterpoladorNewton:
    """
    Uma classe de implementação de interpolação usando o método de Newton
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
        self.b = list() # Lista dos coefiecentes

    def estimar_print(self, t):
        result = self.estimar(t)
        print(f"f({t}) = {result}")

    def estimar(self, t): # Estima f(t)
        """
        Estima f(t) utilizando o método de interpolação de Newton
        usando os parâmetros (b) calculados anteriormente

        Parâmetros:
        - t: o valor para qual a estimativa será calculada

        Retorna:
        - A estimativa de f(t)
        """
        
        if not self.b: # Se a lista b estiver vazia
            self.calculaParametros()

        # f(t)= b1 + b2(t - x1) + ... + bn(t - x1)(t - x2)...(t - xn-1)
        result = self.b[0]
        for i in range(1, self.n):
            aux = self.b[i]
            for j in range(i):
                aux*=(t - self.x[j])
            result+=aux

        return result
    
    def calculaParametros(self):
        """
        Calcula os parâmetros do método de Newton
        """
        self.b = list()
        self.__f(0, self.n - 1)

    def __f(self, i, j):
        """
         Função recursiva para calcular valores de b (Diferenças divididas finitas)
         Função equivalente à f(x), sendo x um vetor de xi à xj
         Como x está armazenado no objeto, é necessário apenas
         determinar o intervalo de x (i e j)

         Parâmetros:
         - i: Index inicial
         - j: Index final

         Retorna:
         - O valor calculado
        """

        if i == j: # Caso f(xn), ou seja o intervalo representa apenas um valor

            # Podemos dizer que esse é o cálculo número 0 da recursividade,
            # pois nessa chamada conseguimos retornar diretamente o valor
            # da diferença dividida que será y[i]

            result = self.y[i]
            if i == 0: # Caso f(x1) 
                self.b.append(result) # Encontramos o primeiro coeficiente (b1)

            return result

        # Cálculando a diferença dividida recursivamente
        f1 = self.__f(i, j - 1) # f(xi à x(j-1))
        f2 = self.__f(i + 1, j) # f(x(i+1) à xj)
        result = (f2 - f1) / (self.x[j] - self.x[i])

        if i == 0: # Caso f(x1, x2 ... xn)
            self.b.append(result) # Encontramos o próximo coeficiente para b

        return result
    
    def __str__(self):
        return f"InterpoladorNewton[Número de pontos: {self.n}; b: {np.round(self.b, 5)}]"

# Busca o intervalo da raiz de func dentro de vetor
def buscaIncremental(func, vetor):
    n = len(vetor)
    i = 0
    a = vetor[i]
    b = vetor[i+1]

    # Enquanto não achar o subintervalo que possui a raíz ao nível aceito de erro, usando o deslocamento (fx)
    while func(a)*func(b) >= 0:
        # Próximo subintervalo
        i+=1     
        
        # Se percorreu todos subintervalos e não foi encontrado
        if (i >= n - 1): 
            return (a, b)
        
        a = vetor[i]
        b = vetor[i+1]

    return (a, b)

x = [24, 25, 26, 27]
y = [89, 124, 154, 165]
# Número a ser encontrado
fx = 130 

# Criando o objeto InterpoladorNewton com base nos vetores x e y
interpoladorNewton = InterpoladorNewton(x, y)
# Calcula e armazena o vetor de parametros (b)
interpoladorNewton.calculaParametros()
parametros = interpoladorNewton.b
n = interpoladorNewton.n

# Criando o vetor do intervalo e o dividindo em 1000 subintervalos
vetor = np.linspace(x[0], x[n-1], 1001)

# Declaração da função
func = lambda x: interpoladorNewton.estimar(x) - fx

(a, b) = buscaIncremental(func, vetor)

print(f"Subintervalo onde a raíz se encontra: [{a} : {b}]")
print(f"f({(a+b)/2}) = {func((a+b)/2) + fx}")