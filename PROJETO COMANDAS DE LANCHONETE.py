#CONTROLE DE COMANDAS EM LANCHONETE
lista_produto=[]
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
        print('\n<<Vamos com o seu "{}°" pedido '.format(num))
        lanche = input('Ecolha o lanche que deseja incluir: 1, 2, 3, 4: ')
        if lanche !="1" and lanche!="2" and lanche!="3" and lanche!="4":
          print('Escolha uma opção dentro do cardapio')
          continue #continua perguntado uma das opções do menu

        else:
          qtd = int(input('Entre com a quantidade(em numeros inteiros) desejada: '))
          if lanche == '1':
              lanche= "xburguer"
              preco=10.90 #preco recebe o preco informado no cardapio
          elif lanche =='2':
              lanche = 'xburguer'
              preco = 9.90
          elif lanche =='3':
              lanche = 'xsalada'
              preco=9.90
          elif lanche =='4':
              lanche = 'xtudo'
              preco = 15.90
    except ValueError:
      print('Entre com um valor numerico ')

    dicionario ={   'pedido':       num,# o dicionario integra os valores do input
                    'lanche':    lanche,
                    'quantidade ':  qtd,
                    'preco':      preco,
                       }
    lista_produto.append(dicionario.copy()) #"keys" e "values" são incorporados a lista de produto
    break #para o laço d repetição

#***********************inicio da funcão d consulta*****************************
def consulta_pedido():
    print('<<Veja todos os laches')
    print()
    for lanche in lista_produto:  # para variavel'lanches' na lista de produtos:
        for key, value in lanche.items():# para  posiçoes 'key e value' no 'lanche' os items
          print('{} = {}'.format(key, value))# imprima todas as chaves e valores

#*********************incio da função cancelar produto**************************
def cancelar_pedido():
  num=int(input('\n<<Entre com o numero do pedido para cancelamento: ' ))
  for p in lista_produto:
    if p['pedido']==num:#se o valor"p" na posição "pedido" for igual a "mun" escolha
      lista_produto.remove(p)#exclua da lista de produtos
      print(f"O pedido numero '{p}' foi CANCELADO")

#***********************inicio do programa principal****************************
print('*'*55)
cardapio()
while True:
    print()
    menu=input('<<O que voce deseja fazer? \n'+
              '0-Ver o cardapio\n'+
              '1-Fazer o pedido\n'+
              '2-Consultar o pedido\n'+
              '3-Cancelar o pedido\n'+
              '4-Encerra o sistema\n'+
              '>>')
    if menu == '1': # na opcao '2' e gerado o 'num' como variavel global do pedido
        num=num+1
        entrada_pedido(num )
    elif menu=='2': # na opção '3' e gerado a consulta geral de todos os pedidos
        consulta_pedido()
    elif menu== "3":
        cancelar_pedido()
    elif menu=='0':
        cardapio()
    elif menu == "4":
        break #encerra o programa
    else:
        print('Digite uma opção valada')
        continue
print()
soma = 0
quantia = 0
for lanche in lista_produto:
  if 'quantidade' in lanche:
    quantia=quantia + lanche['quantidade']
print(f'A quantidade de lanche e = {quantia}')

print('\nVeja os detalhes das vendas do dia ')
for lanche in lista_produto:
  for k,v in lanche.items():
    print(f'{k}={v}')

for lanche in lista_produto:
  if 'preco' in lanche:
    soma += lanche['preco']
print(f"O total arrecadado foi = R$ {soma}")


print(f'A quantidade de lanche e = {quantia}')

print('****************OBRIGADO! VOLTE SEMPRE!****************')
