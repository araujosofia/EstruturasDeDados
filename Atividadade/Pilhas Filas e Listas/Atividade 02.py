from collections import deque

# Inicializa a fila de pedidos como uma deque (fila eficiente)
fila_de_pedidos = deque()

# Função para adicionar um pedido à fila
def adicionar_pedido(fila, pedido):
    fila.append(pedido)

# Adicionando pedidos
adicionar_pedido(fila_de_pedidos, "Martelo Encantado")
adicionar_pedido(fila_de_pedidos, "Pinça Teleportadora")
adicionar_pedido(fila_de_pedidos, "Chave de Fenda Sônica")

# Visualizando a fila
print("\nFila de Pedidos dos Gnomos:")
print(fila_de_pedidos)

# Função para processar (remover e retornar) o primeiro pedido
def processar_pedido(fila):
    return fila.popleft()

# Processando o próximo pedido
pedido_atendido = processar_pedido(fila_de_pedidos)
print("\nPedido atendido:")
print(pedido_atendido)

# Função para verificar se a fila está vazia
def fila_vazia(fila):
    return len(fila) == 0

# Verificar se a fila ainda possui pedidos
print("\nA fila ainda tem pedidos?")
print(fila_vazia(fila_de_pedidos))

# Visualizar fila restante
print("\nPedidos restantes na fila:")
print(fila_de_pedidos)

# Processando os pedidos restantes
print("\nProcessando pedidos restantes:")
while not fila_vazia(fila_de_pedidos):
    print("Atendido:", processar_pedido(fila_de_pedidos))

# Verificar fila ao final
print("\nFila vazia ao final?")
print(fila_vazia(fila_de_pedidos))

