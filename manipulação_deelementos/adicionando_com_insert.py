lista_de_compras = ["banana", "papal", "biscoito", "pizza", "lapiz", "computador"]  # crio a variável de uma lista de compras
novo_item = input("Digite uma nova compra: ")  # crio uma variável onde a pessoa vai digitar um novo item
local_adicionado = int(input("digite onde você quer colocar esse item na lista: "))  # crio uma variável onde a pessoa vai digitar onde quer colocar o item que ele escrevel
lista_de_compras.insert(local_adicionado,novo_item)  # adiciono o novo item digitado a lita usando o inset para colocar na posição desejada
print(lista_de_compras)  # exibo a lista de compras com os itens adicionados