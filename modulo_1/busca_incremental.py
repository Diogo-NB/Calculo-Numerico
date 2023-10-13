# -*- coding: utf-8 -*-
import numpy as np
"""
@author: Diogo Nunes Batista

Módulo 1 - Trabalho 1
Estimação de raízes pelo método de busca incremental.
"""

# Declaração da função
def func(x): return 2*np.log(x-1) + 3

# Criando o vetor do intervalo e o dividindo em 100 subintervalos
vetor = np.linspace(1.002, 2, 101)

i = 0
a = vetor[i]
b = vetor[i+1]

# Enquanto não achar o subintervalo que possui a raíz ao nível aceito de erro
while func(a)*func(b) >= 0:
    # Próximo subintervalo
    i+=1     
    
    # Se percorreu todos subintervalos e não foi encontrado
    if (i >= vetor.size - 1): 
        print("Não foi encontrada raíz")
        break
    
    a = vetor[i]
    b = vetor[i+1]
else:
    print("Subintervalo onde a raíz se encontra: [", a,':',b, ']')

    
    








