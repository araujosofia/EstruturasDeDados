# Inicializa o catálogo mágico como uma lista vazia
catalogo_magico = []

# Função para adicionar um livro ao final do catálogo
def adicionar_livro(catalogo, livro):
    catalogo.append(livro)  # Adiciona o livro ao final da lista

# Adicionando livros ao catálogo
adicionar_livro(catalogo_magico, "O Feitiço da Lua Crescente")
adicionar_livro(catalogo_magico, "A Jornada do Unicórnio Perdido")
adicionar_livro(catalogo_magico, "Segredos da Floresta Encantada")

# Visualizando o catálogo
print("Catálogo Mágico:")
print(catalogo_magico)

# Função para buscar um livro por índice
def buscar_livro(catalogo, indice):
    return catalogo[indice]

# Buscando o livro na posição 1
livro_encontrado = buscar_livro(catalogo_magico, 1)
print("\nLivro encontrado na posição 1:")
print(livro_encontrado)

# Remover o livro "A Jornada do Unicórnio Perdido"
catalogo_magico.remove("A Jornada do Unicórnio Perdido")

# Visualizar catálogo atualizado
print("\nCatálogo após remoção:")
print(catalogo_magico)

# Função para verificar a presença de um livro
def verificar_livro(catalogo, livro):
    return livro in catalog
