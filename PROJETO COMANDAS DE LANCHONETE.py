#CONTROLE DE COMANDAS EM LANCHONETE
lista_produto=[]
lista1=[]
dicionario={}
dic=[   {"cod":"1","lanche":"xburguer","preco":10.90},
        {"cod":"2","lanche":"xbacon  ","preco":9.90},
        {"cod":"3","lanche":"xsalada ","preco":9.90},
        {"cod":"4","lanche":"xtudo   ","preco":15.90},
        {"cod":"5","lanche":"refriger","preco":5.90}]


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

def entrada_pedido(num):
  soma_preco=0
  print("NOVO PEDIDO".center(55,"-"))
  print("S-SAIR                                         P-PAGAR\n")
  while True:
    try:
      lanche = input('Digite o código do lanche que deseja>>').upper()
      if lanche[0] not in "12345SP":
        print('Escolha uma opção dentro do cardapio')
      elif lanche =="P":
        print(f"VALOR PAGO R$ {soma_preco:.2f}".rjust(55))
        lista_produto.extend(lista1)
        lista1.clear()
        break
      elif lanche[0]=="S":
        print("CANCELADO".rjust(55))
        lista1.clear()
        break
      else:
        qtd = int(input('Digite a quantidade desejada incluir>>'))
        num+=1
        for item in dic:
            if item["cod"]==lanche:
                lanche=item["lanche"]
                preco = item['preco']*qtd
                soma_preco+=preco
                print(f"COMANDA n° {num}".rjust(55))
                print(f"{qtd}                    {lanche}",end="")
                print(f"{preco:.2f}".rjust(26))
                print("SubTotal",end="")
                print(f"{soma_preco:.2f}".rjust(47))
                dicionario = {'Comanda': num,
                              'Lanche': lanche,
                              'Quantidade': qtd,
                              'Preco': preco}
                lista1.append(dicionario.copy())
    except ValueError:
        print('Entre com um valor numerico ')
        continue


#//inicio da funcão d consulta

def consulta_pedido():
    try:
      print("CONSULTAR COMANDA".center(55,"-"))
      print("0-Todas".rjust(55))

      com=int(input("\nDigite o numero da comanda>>"))
      if com != 0:
        print("Comanda          Lanche        Quantidade         Preco")
        for lanche in lista_produto:
            if lanche["Comanda"] == com:
              print(f'N° {lanche["Comanda"]}            {lanche["Lanche"]}           {lanche["Quantidade"]}              {lanche["Preco"]:.2f} ')
              break
      else:
        print("Comanda          Lanche        Quantidade         Preco")
        for lanche in lista_produto:
          print(f'Nª {lanche["Comanda"]}            {lanche["Lanche"]}           {lanche["Quantidade"]}              {lanche["Preco"]:.2f} ')
        return
    except ValueError:
      print("COMANDA INVALIDA")


#//incio da função cancelar produto

def cancelar_pedido():
  print("EXCLUIR COMANDA".center(55,"-"))
  print("0-Sair".rjust(55))
  num=int(input('\nDigite o numero da comanda>>'))
  if num!=0:
    print("Comanda          Lanche        Quantidade         Preco")
    for lanche in lista_produto:
        if lanche["Comanda"] == num:
          print(f'N° {lanche["Comanda"]}            {lanche["Lanche"]}           {lanche["Quantidade"]}              {lanche["Preco"]:.2f} ')
          break

    perg=input("\n0-SAIR                                       1-EXCLUIR\n"+">>").upper()
    if perg[0]in"1E":
      lista_produto.remove(lanche)#exclua da lista de produtos
      print("EXCLUIDA".rjust(55))
    else:
      print("Voltar".rjust(55))
      return
  else:
    print("COMANDA INVALIDA!")


#//inicio do programa principal

print('*'*55)
cardapio()
while True:
    print()
    print("MENU PRINCIPAL".center(55,"-"))
    print('1-Pedir      2-Consultar      3-Excluir      0-Cardapio')
    menu=input('                                                   Sair\n'+
              '>>').upper()
    if menu == '1':
        num=len(lista_produto)
        entrada_pedido(num)
    elif menu=='2':
        consulta_pedido()
    elif menu=="3":
        cancelar_pedido()
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





