# programa de controle de pedidos de lanche em lanchonbete usando dicionarios
lista_produto = []  # declaração da lista que vai receber um dicionario
num = 0  # declaraação da variavel global que vai receber o codigo do pedido
# controle de compras e estoque em lanchonetes
soma = 0
quantia = 0


def cardapio():  # inicio da função que imprime o cardapio
    print('*' * 55)
    print('              +---+----------+---------+')
    print('              |COD|  PRODUTO |  PREÇO  |')
    print('              +---+----------+---------+')
    print('              | 1 | XBURGUER | R$10.90 |')
    print('              | 2 | X BACON  | R$9.90  |')
    print('              | 3 | X SALADA | R$9.90  |')
    print('              | 4 | X TUDO   | R$15.90 |')
    print('              +---+----------+---------+')
    print('*' * 55)


def entrada_pedido(num):  # função de entrado com o parametro do codigo recebido pela entra de pedido
    global soma, quantia  # as variaveis globais retornam o acumulado da soma e da quantidade
    while True:  # inicio do tratamento de erros
        try:
            print('\nVamos com o seu {}° pedido '.format(num))
            lanche = input(
                'Ecolha o lanche que deseja incluir: 1, 2, 3, 4:>> ')  # lance recebe a escolha dentro do menu em cardapio
            if lanche != "1" and lanche != "2" and lanche != "3" and lanche != "4":
                print('Escolha uma opção dentro do cardapio')
                continue  # continua perguntado uma das opções do menu

            else:
                qtd = int(input(
                    'Entre com a quantidade(em numeros inteiros) desejada: '))  # quantidade recebe quanto vc deseja comprar

                # NESSA SEQUENCIA DECIOES DEFINIMOS O LANCHE A PARTIR DO CODIGO NO CARDAPIO
                if lanche == '1':
                    lanche = "xburguer"
                    preco = 10.90  # preco recebe o preco informado no cardapio
                    quantia += qtd
                    soma += preco * qtd
                elif lanche == '2':
                    lanche = 'xburguer'
                    preco = 9.90
                    quantia += qtd
                    soma += preco * qtd
                elif lanche == '3':
                    lanche = 'xsalada'
                    preco = 9.90
                    quantia += qtd
                    soma += preco * qtd
                elif lanche == '4':
                    lanche = 'xtudo'
                    preco = 15.90
                    soma += preco * qtd
                    quantia += qtd
        except ValueError:
            print('Entre com um valor numerico ')

        dicionario = {'pedido': num,  # o dicionario integra os valores do input
                      'lanche': lanche,
                      'quantidade ': qtd,
                      'preco': preco,
                      }

        lista_produto.append(
            dicionario.copy())  # o didionario recebe todas as "keys" e "values" e é incorporado a lista de produto sendo separados pelo codigo "num"
        break  # para o laço d repetição


# inicio da funcão d consulta
def consulta_pedido():
    print('Veja todos os laches')
    print()
    for lanche in lista_produto:  # para variavel'lanches' na lista de produtos:
        for key, value in lanche.items():  # para  posiçoes 'key e value' no 'lanche'.os items
            print('|{}: {}|', end=''.format(key, value))  # imprima todos os lanches


# função para ler todos preços de cada numero de pedido e calcular a soma total
def ajuste():
    global soma, quantia

    ped = int(input('\nEntre com o numero do pedido'))
    for p in lista_produto:
        if p['pedido'] == ped:

            lanche = input('Ecolha o lanche que deseja incluir: 1, 2, 3, 4:>> ')[
                0]  # lance recebe a escolha dentro do menu em cardapio
            if lanche != "1" and lanche != "2" and lanche != "3" and lanche != "4":
                print('Escolha uma opção dentro do cardapio')
                continue  # continua perguntado uma das opções do menu
            else:

                qtd = int(input(
                    'Entre com a quantidade(em numeros inteiros) desejada: '))  # quantidade recebe quanto vc deseja comprar

                # NESSA SEQUENCIA DECIOES DEFINIMOS O LANCHE A PARTIR DO CODIGO NO CARDAPIO
                if lanche == '1':
                    lanche = "xburguer"
                    preco = 10.90  # preco recebe o preco informado no cardapio
                    quantia += qtd
                    soma += preco * qtd
                elif lanche == '2':
                    lanche = 'xbacon'
                    preco = 9.90
                    quantia += qtd
                    soma += preco * qtd
                elif lanche == '3':
                    lanche = 'xsalada'
                    preco = 9.90
                    quantia += qtd
                    soma += preco * qtd
                elif lanche == '4':
                    lanche = 'xtudo'
                    preco = 15.90
                    soma += preco * qtd
                    quantia += qtd

    dicionario = {'pedido': ped,  # o dicionario integra os valores do input
                  'lanche': lanche,
                  'quantidade ': qtd,
                  'preco': preco,
                  }

    lista_produto.append(dicionario.copy())


# programa principal
print('*' * 55)
cardapio()
while True:
    print()
    menu = input('O que voce deseja fazer? \n' +
                 '1-Fazer o pedido\n' +
                 '2-Consultar o pedido\n' +
                 '3-Ajustar pedido\n' +
                 '0-encerra o sistema\n' +
                 '>>')
    if menu == '1':  # na opcao '2' e gerado o 'num' como variavel global do pedido
        num = num + 1
        entrada_pedido(num)
    elif menu == '2':  # na opção '3' e gerado a consulta geral de todos os pedidos
        consulta_pedido()
    elif menu == "3":
        ajuste()
    elif menu == '0':
        break  # encerra o programa
    else:
        print('digite uma opção valada')
        continue
print()

# print('Foram servidos {} pedidos'.format(len(lista_produto)))
print('Foram vendidos {} lanches e o total arrecadado foi R$ {:.2f}'.format(quantia, soma))
# print('o valor total dos pedido e {} '.format(soma))
print('\nVeja os detalhes das vendas do dia ')
for lanche in lista_produto:
    for k, v in lanche.items():
        print(f'{k}={v}', end=" , ")
