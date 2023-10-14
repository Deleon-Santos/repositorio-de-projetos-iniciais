#CONTROLE DE COMANDAS EM LANCHONETE
lista_produto=[]
dicionario={}
#dicionario com os itens e precos
dic=[   {"cod":"1","lanche":"xburguer","preco": 10.90},
        {"cod":"2","lanche":"xbacon","preco": 9.90},
        {"cod":"3","lanche":"xsalada" ,"preco":9.90},
        {"cod":"4","lanche":"xbacon","preco": 9.90},
        {"cod":"5","lanche":"refrigerante","preco":5.90}]
num = 0

#****************inicio da função que imprime o cardapio************************
def cardapio():
    print('*'*55)
    print('              +---+----------+---------+')
    print('              |COD|  PRODUTO |  PREÇO  |')
    print('              +---+----------+---------+')
    print('              | 1 | XBURGUER | R$10.90 |')
    print('              | 2 | X BACON  | R$9.90  |')
    print('              | 3 | X SALADA | R$9.90  |')
    print('              | 4 | X TUDO   | R$15.90 |')
    print('              +---+----------+---------+')
    print('*'*55)

#**************************inicio da função pedido******************************
def entrada_pedido(num): #função de entrado com o parametro do codigo recebido pela entra de pedido
  while True:#laço para tratamento de erros
    try:
        print(f"COMANDA n° {num}".rjust(55,"_"))
        lanche = input('Digite o código do lanche que deseja incluir________>>')
        if lanche !="1" and lanche!="2" and lanche!="3" and lanche!="4":
            print('Escolha uma opção dentro do cardapio')
            continue #continua perguntado uma das opções do menu

        else:
             qtd = int(input('Digite a quantidade desejada incluir________________>>'))
             for item in dic:
                if item["cod"]==lanche:
                    lanche=item["lanche"]
                    preco = item['preco']
                    dicionario = {'Comanda': num,
                                  'Lanche': lanche,
                                  'Quantidade': qtd,
                                  'Preco': preco}

                    lista_produto.append(dicionario.copy())
                    break
    except ValueError:
        print('Entre com um valor numerico ')
        continue
    break

#***********************inicio da funcão d consulta*****************************
def consulta_pedido():

    print("CONSULTAR COMANDAS".center(55))
    com=int(input("Digite o numero da comanda__________________________>>"))

    for lanche in lista_produto:
        if lanche["Comanda"] == com:
            for key, value in lanche.items():  # para  posiçoes 'key e value' no 'lanche' os items
                print(f'{key}')
                print(f'{value}'.rjust(55,"-"))

        else:
            print("Esta comanda não foi encontrada")


#*********************incio da função cancelar produto**************************
# def cancelar_pedido():
#   num=int(input('\n<<Entre com o numero do pedido para cancelamento: ' ))
#   for p in lista_produto:
#     if p['pedido']==num:#se o valor"p" na posição "pedido" for igual a "mun" escolha
#       lista_produto.remove(p)#exclua da lista de produtos
#       print(f"O pedido numero '{p}' foi CANCELADO")

#***********************inicio do programa principal****************************
print('*'*55)
cardapio()
while True:
    print()
    menu=input('                     MENU INICIAL \n'+
              '1-Cardapio       2-Pedido        3-Consulta        Sair\n'+
              ''
              '>>').upper()


    if menu == '2': # na opcao '1' e gerado o 'num' como variavel global do pedido
        num=num+1
        entrada_pedido(num )
    elif menu=='3': # na opção '2' e gerado a consulta geral de todos os pedidos
        consulta_pedido()
    # elif menu== "3":
    #     cancelar_pedido()
    elif menu=='1':
        cardapio()
    elif menu[0] == "S":
        break #encerra o programa
    else:
        print('Digite uma opção valada')
        continue
print()
soma = 0
quantia = 0
print"Produto                    Quantidade                          Valor"
for lanche in lista_produto:
    p=lanche["Lanche"]
    #for lanche in dicio:
    #if lanche['Lanche']== "xburguer":
   #print(lanche["Lanche"])
    soma += lanche['Quantidade']

    quantia+= lanche["Preco"]

    print(f"{soma}                   {p} ,                       {quantia}")

#print(f"{soma}, {}")
#
# print('****************OBRIGADO! VOLTE SEMPRE!****************')
