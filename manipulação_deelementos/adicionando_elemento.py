

integrantes = []  # crio a variável 'integrantes'
integrante_novo = input("Digite o nome do aluno para o seu grupo(lembrando que o limite é de cinco pessoas, caso não tenha um total de cinco pessoas digite 'sair' para encerrar): ")  # crio uma variável e faço uma pergunta para e pesoa colocar um nome do grupo
integrantes.append(integrante_novo)  # adiciono o que foi colocado no integrante_novo ao integrantes
for i in range (4):  #  uso a função for para repetir 4 vezes pois os grupos só podem ter até cinco membros
    if integrante_novo.upper() == 'sair':  #  si a pessoa digitar 'sair' a função acaba
        break  #  função de encerrar toda a função
    integrante_novo = input("Digite o nome do aluno para o seu grupo:")  #  volto a perguntar o nome dos proximos integrantes
    integrantes.append(integrante_novo)  #  continuo adicionando o que foi digitado no integrante_novo ao integrantes
print("membros do grupo:", integrantes)  #  exibo todos os nomes do grupo