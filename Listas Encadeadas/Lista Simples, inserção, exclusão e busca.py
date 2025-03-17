class ListaSimples:
    """Implementação de uma Lista Encadeada Simples."""
    def __init__(self):
        self.head = None  # Inicializa a lista vazia

    def inserir(self, data):
        """Insere um novo nó no final da lista."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def excluir(self, data):
        """Exclui um nó que contém o valor especificado."""
        if not self.head:
            print("Lista vazia, nada para excluir.")
            return
        if self.head.data == data:  # Caso especial: remover o primeiro nó
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != data:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next  # Remove o nó encontrado
        else:
            print(f"Valor {data} não encontrado na lista.")

    def buscar(self, data):
        """Busca um valor na lista e retorna True se encontrado."""
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def exibir(self):
        """Exibe todos os elementos da lista."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
