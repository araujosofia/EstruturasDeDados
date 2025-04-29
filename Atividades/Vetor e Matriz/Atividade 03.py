# Criar um vetor com 10 elementos inteiros positivos
vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Solicitar um valor ao usuario
valor_procurado = int(input("Digite um valor inteiro positivo: "))

# Verificar se o valor existe no vetor e exibe o resultado
if valor_procurado in vetor:
    print(f"O valor {valor_procurado} existe no vetor.")
else:
    print(f"O valor {valor_procurado} não existe no vetor.")
