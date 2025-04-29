 # Criar uma matriz 3x3 com elementos reais positivos
matriz =[ [1.0, 2.0, 3.0],
          [4.0, 5.0, 6.0],
          [7.0, 8.0, 9.0]
]

#Calcular e exibir a soma dos elementos de cada linha
for i in range(3):
    soma_linha = sum(matriz[i])
    print("soma da linha", i + 1, ":", soma_linha)
