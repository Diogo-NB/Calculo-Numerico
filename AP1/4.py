import numpy as np

# Retorna um novo vetor ao "isolar" a variável da posição i
def isolar(i: int, v: object):
    new_v = np.array(v * (-1/v[i]), dtype= "float64")
    new_v[i] = 0.0
    return new_v

# Printa o vetor x
def print_x(v: object):
    for i in range(v.shape[0]):
        print(("x" + str(i + 1) + " ≈"), round(v[i], 5))

# Retorna uma solução x para o sistema Ax = c usando o método de gauss_seidel
def gauss_seidel(A, c, x, tolerancia):
    # Ax = c
    # Parametro x é a estimativa inicial de solução para x 
    mr = 1

    A = np.array(A, dtype="float64")
    c = np.array(c, dtype="float64")
    x = np.array(x, dtype="float64")

    # Número de linhas 
    nl = A.shape[0]
    # Número de colunas para a matriz C
    nc = nl

    C = np.zeros((nl, nc))
    g = np.zeros(nl)

    # Encontrando a matriz C e o vetor g
    for i in range(nl):
        aux = isolar(i, A[i])
        for j in range(nc):
            C[i][j] = aux[j]
        g[i] = c[i] / A[i][i]

    # Contador
    k = 0

    # Iterando
    while mr > tolerancia:
        x_anterior = np.copy(x) # Vetor x da iteração anterior

        # Nova estimação de x: x = Cx + g
        for i in range(nl):
            x[i] = np.dot(C[i], x) + g[i]

        # Cálculo vetor m
        m = abs(x - x_anterior)
        
        # Calculo de erro
        mr = max(m) / max(x)
        
        k+=1 # Incrementando contador

    print("Número de iterações =", k)
    print_x(x)

    return x

A = [
    [10, 2, -1], 
    [-3, -6, 2],
    [1, 1, 5],
    ]
c = [6, 2, 8]
x = [1, 0, -3]

x = gauss_seidel(A, c, x, 0.0001)
print(np.round(x, 5))
print(np.allclose(np.dot(A, x), c, atol=0.0001))