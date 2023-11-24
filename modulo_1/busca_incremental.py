import numpy as np
"""
@author: Diogo Nunes Batista

Módulo 1 - Trabalho 1
Estimação de raízes pelo método de busca incremental.
"""

def buscaIncremental(func, vetor, fx = 0): # fx é o número a ser buscado
    n = len(vetor)
    i = 0
    a = vetor[i]
    b = vetor[i+1]

    # Enquanto não achar o subintervalo que possui a raíz ao nível aceito de erro, usando o deslocamento (fx)
    while (func(a) - fx)*(func(b) - fx) >= 0:
        # Próximo subintervalo
        i+=1     
        
        # Se percorreu todos subintervalos e não foi encontrado
        if (i >= n - 1): 
            return
        
        a = vetor[i]
        b = vetor[i+1]

    return (a, b)

def trabalho_1():
    # Declaração da função
    def func(x): return 2*np.log(x-1) + 3

    # Criando o vetor do intervalo e o dividindo em 100 subintervalos
    vetor = np.linspace(1.002, 2, 101)
    (a, b) = buscaIncremental(func, vetor)
    print(f"Intervalo encontrado: {[a,b]}")

if __name__ == "__main__":
    trabalho_1()