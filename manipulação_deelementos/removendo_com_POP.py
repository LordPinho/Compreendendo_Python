lista_de_compras = ["banana", "papal", "biscoito", "pizza", "lapiz", "computador"]  # crio a variável de uma lista de compras novamente
local_removido = int(input("caso queira remover um item da lista, digite onde ele está localizado para que ele seja removido: "))  # crio uma variável onde a pessoa vai digitar onde quer remover um item da lita pela sua posilção
lista_de_compras.pop(local_removido)  # removo um item da lista de acordo com o número digitado anteriormente
print(lista_de_compras)  # exibo a lista de compras com os itens removidos