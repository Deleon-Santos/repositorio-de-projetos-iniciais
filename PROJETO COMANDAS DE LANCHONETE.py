
#CONTROLE DE COMANDAS EM LANCHONETE
lista_produto=[]
lista1=[]
dicionario={}
# import json
dic=[   {"cod":"1","lanche":"xburguer","preco":10.90},
        {"cod":"2","lanche":"xbacon  ","preco":9.90},
        {"cod":"3","lanche":"xsalada ","preco":9.90},
        {"cod":"4","lanche":"xtudo   ","preco":15.90},
        {"cod":"5","lanche":"refriger","preco":5.90}]

com=0
#inicio da função que imprime o cardapio
def cardapio():
    print("BEM-VINDO AO BOCA NERVOSA".center(55,"*"))
    print('+-------------+-----------------+---------------------+')
    print('|   CODIGO    |      PRODUTO    |        PREÇO        |')
    print('+-------------+-----------------+---------------------+')
    print('|     1       |     XBURGUER    |       R$10.90       |')
    print('|     2       |     X BACON     |       R$9.90        |')
    print('|     3       |     X SALADA    |       R$9.90        |')
    print('|     4       |     X TUDO      |       R$15.90       |')
    print('|     5       |   REFRIGERANTE  |       R$5.90        |')
    print('+-------------+-----------------+---------------------+')
    print("*******************************************************")


#//inicio da função pedido
def entrada_pedido(com):
    soma2=0
    num=0
    print("NOVO PEDIDO".center(55,"-"))
    print("S-SAIR                C-CANCELAR                P-PAGAR\n")
    print(f"COMANDA n° {com}".rjust(55))

    while True:
        try:
            lanche = input('Digite o código do lanche que deseja>>').upper()
            if lanche[0] not in "12345SPC":
                print('Escolha uma opção dentro do cardapio')

            elif lanche[0]=="C":
                num1=int(input('\nDigite o numero do item>>'))
                for lanche in lista1:
                    if lanche["Comanda"] == num1:
                        soma2-=lanche["Preco"]
                        print(f'N° {lanche["Comanda"]}            {lanche["Lanche"]}          -{lanche["Quantidade"]}          -R$ {lanche["Preco"]:.2f} ')
                        lista1.remove(lanche)#exclua da lista de produtos
                print("REMOVIDO".rjust(55))
                continue

            elif lanche =="P":
                print(f"VALOR PAGO R$ {soma2:.2f}".rjust(55))
                lista_produto.extend(lista1)
                lista1.clear()
                break

            elif lanche=="S":
                lista1.clear()
                print("PEDIDO CANCELADO".rjust(55))
                break

            else:
                qtd = int(input('Digite a quantidade desejada incluir>>'))
                num+=1
                for item in dic:
                    if item["cod"]==lanche:
                        lanche=item["lanche"]
                        preco = item['preco']*qtd
                        soma2+=preco
                        dicionario = {'Pedido': com,
                                    'Comanda': num,
                                    'Lanche': lanche,
                                    'Quantidade': qtd,
                                    'Preco': preco,}
                        lista1.append(dicionario.copy())

                        print("Item          Lanche          Quantidade          Preco")
                        for lanche in lista1:
                            pre=lanche["Preco"]
                            print(f'N° {lanche["Comanda"]}         {lanche["Lanche"]}              {lanche["Quantidade"]}',end="")
                            print(f"R$ {pre:.2f}".rjust(19))
                        print("SubTotal",end="")
                        print(f"R$ {soma2:.2f}".rjust(47))
        except ValueError:
            print('Entre com um valor numerico ')
            continue


#//inicio da funcão d consulta
def consulta_pedido():
    try:
        print("CONSULTAR COMANDA".center(55,"-"))
        print("0-Todas".rjust(55))
        com1=int(input("\nDigite o numero da comanda>>"))
        if com1 == 0:
            print("Com     Item         Lanche       Quantidade      Preco")
            for lanche in lista_produto:
                p=lanche["Preco"]
                print(f'{lanche["Pedido"]}        {lanche["Comanda"]}          {lanche["Lanche"]}           {lanche["Quantidade"]}',end="")
                print(f"R$ {p:.2f}".rjust(15))
        else:
            print("Com     Item         Lanche       Quantidade      Preco")
            for lanche in lista_produto:
                if lanche["Pedido"] == com1:
                    p=lanche["Preco"]
                    print(f'{lanche["Pedido"]}        {lanche["Comanda"]}          {lanche["Lanche"]}           {lanche["Quantidade"]}',end="")
                    print(f"R$ {p:.2f}".rjust(15))
    except ValueError:
        print("Nao encontrada")

#//incio da função cancelar produto
# with open('cardapio.txt', 'w') as arquivo:
#     json.dump(dic, arquivo)
print('*'*55)
cardapio()
while True:
    print()
    print("MENU PRINCIPAL".center(55,"-"))
    print('1-Pedir               2-Consultar            0-Cardapio')
    menu=input('                                                   Sair\n'+
              '>>').upper()
    if menu == '1':
        com+=1
        entrada_pedido(com)
    elif menu=='2':
        consulta_pedido()
    elif menu=='0':
        cardapio()
    elif menu[0] == "S":
        break #encerra o programa
    else:
        print('OPÇÃO INVALIDA!')
        continue

print("VENDA TOTAL DO DIA".center(55))
qtd_t=0
som_t=0
for l in ["xburguer","xbacon  ","xsalada ","xtudo   ","refriger"]:
    qtd=0
    somas=0
    for lanche in lista_produto:
        if lanche["Lanche"]==l and lanche["Quantidade"]!=0:
            qtd+=lanche["Quantidade"]
            somas+=lanche["Preco"]
    print(f"{l}                  {qtd}",end="")
    print(f"{somas:.2f}".rjust(28))
    qtd_t+=qtd
    som_t+=somas
print()
print(f"Total Lenches",end="")
print(f"{qtd_t}".rjust(14))
print(f"Soma Total ",end="")
print(f"R$ {som_t:.2f}".rjust(44))
print()
print("ENCERRANDO O SISTEMA".center(55))





