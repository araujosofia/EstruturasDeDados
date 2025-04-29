# Inicializa a pilha de cristais como uma lista vazia
torre_de_cristais = []

# Função para empilhar um cristal (adicionar ao topo)
def empilhar_cristal(pilha, cristal):
    pilha.append(cristal)

# Adicionando cristais
empilhar_cristal(torre_de_cristais, "Cristal do Passado")
empilhar_cristal(torre_de_cristais, "Cristal do Presente")
empilhar_cristal(torre_de_cristais, "Cristal do Futuro")

# Visualizando a pilha (topo está no final)
print("\nTorre de Cristais:")
print(torre_de_cristais)

# Função para desempilhar (remover e retornar) o topo da pilha
def desempilhar_cristal(pilha):
    return pilha.pop()

# Utilizando o cristal do topo
cristal_utilizado = desempilhar_cristal(torre_de_cristais)
print("\nCristal utilizado no ritual:")
print(cristal_utilizado)

# Função para verificar se a pilha está vazia
def pilha_vazia(pilha):
    return len(pilha) == 0

# Verificar se ainda há cristais
print("\nAinda há cristais na torre?")
print(pilha_vazia(torre_de_cristais))

# Visualizando pilha restante
print("\nCristais restantes na torre:")
print(torre_de_cristais)

# Utilizando cristais restantes
print("\nUtilizando cristais restantes:")
while not pilha_vazia(torre_de_cristais):
    print("Cristal utilizado:", desempilhar_cristal(torre_de_cristais))

# Verificando se a pilha está vazia no final
print("\nTorre está vazia?")
print(pilha_vazia(torre_de_cristais))
