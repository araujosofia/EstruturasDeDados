# 2) Matriz de caracteres 4x4

# Criando a matriz com compreensão de lista
letras = [chr(i) for i in range(ord('a'), ord('p') + 1)]

# Preenchendo a matriz 4x4
matriz = [letras[i:i+4] for i in range(0, 16, 4)]

# Exibindo a matriz com índices de linha e coluna
print("\nMatriz de caracteres 4x4:")
for i in range(4):
    for j in range(4):
        print(f"{matriz[i][j]}", end=' ')
    print()
