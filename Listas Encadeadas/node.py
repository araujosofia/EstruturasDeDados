cclass Node:
    """Classe que representa um nó da lista encadeada."""
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Referência para o próximo nó
