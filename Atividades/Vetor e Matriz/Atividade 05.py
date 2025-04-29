# Criar uma matriz 5x5 com inteiros positivos e negativos
matriz = [
    [3, -1, 4, 1, 5],
    [-2, 7, 0, -3, 8],
    [6, -5, 9, 2, -4],
    [1, -6, 3, 5, 7],
    [0, 2, -8, 4, 6]
]

# Inicializar o maior elemento com um valor muito baixo
maior_elemento = float('-inf')

# Encontrar o maior elemento na matriz
for linha in matriz:
    for elemento in linha:
        if elemento > maior_elemento:
            maior_elemento = elemento

# Exibir o maior elemento
print("O maior elemento da matriz é:", maior_elemento)
