#                CONTROLE DE COMANDAS EM LANCHONETE
import json
lista_produto = []
lista1 = []
com = 0
dicionario = {}
with open('comanda.txt', 'r') as adic:#abrir arquivo de nome "comanda.TXT" para leitura atribuido a "adic"
    dic = json.load(adic)#o dicionario "dic" = o aquivo JSON para leitura na variavel "adic"

#                         Inicio da funções
def cardapio():
    print("BEM-VINDO AO BOCA NERVOSA".center(55, "*"))
    print('+-------------+-----------------+---------------------+')
    print('|   CODIGO    |      PRODUTO    |        PREÇO        |')
    print('+-------------+-----------------+---------------------+')
    for lanche in dic:  # ler o dicionrio de cadastro e gera o cardapio co o itens atualizados
        cod = lanche["cod"]
        nome_lanche = lanche["lanche"]
        preco = lanche["preco"]
        print(f'|      {cod:<6}        {nome_lanche:<15} R$ {preco:>10.2f}    |')
    print('+-----------------------------------------------------+')

def entrada_pedido(com):
    soma2 = 0
    num = 0
    print("NOVO PEDIDO".center(55, "-"))
    print("S-SAIR                C-CANCELAR                P-PAGAR\n")
    while True:
        try:
            lanche1 = input('Digite o código do lanche que deseja>>').upper()
            # retorna o laço quando as opções sao invalidas
            if lanche1[0] == "S":
                lista1.clear()  # limpa a lista1
                print("Comanda cancelada")
                break

            elif lanche1[0] == "C":
                soma2 = remover(soma2)
                continue
            # encerra o laço e rotorna o valor soma2 a ser pago
            elif lanche1[0] == "P":
                print(f"VALOR PAGO R$ {soma2:.2f}".rjust(55))
                lista_produto.extend(lista1)  # adiciona os novos itens na lista_produto
                lista1.clear()
                break

            else:
                for item in dic:
                    if lanche1 in item["cod"]:
                        num += 1
                        soma2 = coleta(lanche1, soma2, com, num)  # envia e rotorna os parametros
                        continue
        except ValueError:
            print('Entre com um valor numerico ')
            continue

def coleta(lanche1, soma2, com, num):
    try:
        qtd = int(input('Digite a quantidade desejada incluir>>'))
        for item in dic:  # ler e atribui os valores ao dicionario
            if item["cod"] == lanche1:
                lanche = item["lanche"]
                preco = item['preco'] * qtd
                soma2 += preco
                dicionario = {'Pedido': com,
                              'Comanda': num,
                              'Lanche': lanche,
                              'Quantidade': qtd,
                              'Preco': preco, }
                lista1.append(dicionario.copy())
                print(f"COMANDA N°{com}".rjust(55))
                print("Item          Lanche          Quantidade          Preco")
                # ler e escre os valores na tela em forma de tabela
                for lanche in lista1:
                    pre = lanche["Preco"]
                    print(
                        f'N°{lanche["Comanda"]:<7}    {lanche["Lanche"]:<18}',end="")
                    print(f'{lanche["Quantidade"]:>5}           R${pre:>6.2f}')
                print("SubTotal", end="")
                print(f"R${soma2:.2f}".rjust(47))
        return soma2  # retorna o valor soma2
    except ValueError:
        print('Entre com um valor numerico ')

def remover(soma2):
    try:
        num1 = int(input('\nDigite o numero do item>>'))
        for lanche in lista1:
            if lanche["Comanda"] == num1:  # exclui a partir do codigo do item
                soma2 -= lanche["Preco"]
                print(f'N°{lanche["Comanda"]}{lanche["Lanche"]:>15}          -{lanche["Quantidade"]:>3}              -R${lanche["Preco"]:>6.2f} ')
                lista1.remove(lanche)  # exclua da lista de produtos
        print("REMOVIDO".rjust(55))
        return soma2  # retorna a soma2 atualizada
    except ValueError:
        print("Não encontrada")

def consulta_pedido():
    try:
        print("CONSULTAR COMANDA".center(55, "-"))
        print("0-Todas".rjust(55))
        com1 = int(input("\nDigite o numero da comanda>>"))
        if com1 == 0:  # consulta todas as comandas em lista_produto
            print("Com     Item         Lanche       Quantidade      Preco")
            for lanche in lista_produto:
                p = lanche["Preco"]
                print(f'{lanche["Pedido"]}        {lanche["Comanda"]}          {lanche["Lanche"]}         {lanche["Quantidade"]:>2}',end="")
                print(f"        R${p:6.2f}")
        else:  # consulta o numero informado em inpute
            print("Com     Item         Lanche       Quantidade      Preco")
            for lanche in lista_produto:
                if lanche["Pedido"] == com1:
                    p = lanche["Preco"]
                    print(f'{lanche["Pedido"]}        {lanche["Comanda"]}          {lanche["Lanche"]}         {lanche["Quantidade"]:>2}',end="")
                    print(f"        R${p:6.2f}")
    except ValueError:
        print("Nao encontrada")

def total():
    print("VENDA TOTAL DO DIA".center(55))
    qtd_t = 0
    som_t = 0
    for item in dic:  # para cada lanche
        x= item["lanche"]
        qtd = 0
        somas = 0
        for lanche in lista_produto:  # para cada lanche em lista_produto calcuta a quantidade eo preco
            if lanche["Lanche"]==x:
                qtd += lanche["Quantidade"]
                somas += lanche["Preco"]
        if qtd>0:
            print(f"{x}{qtd:>19}                   R${somas:>7.2f}")
            qtd_t += qtd
            som_t += somas
    print()  # escrita dos falores totais
    print(f"Totais           {qtd_t:>10}                   R${som_t:>7.2f}")
    print()
    print("Sair".rjust(55))


# **************************Inicio do programa principal*************************
print('*' * 55)
cardapio()
while True:
    try:
        print()
        print("MENU PRINCIPAL".center(55, "-"))
        print('1-Pedir      2-Consultar      3-Cardapio       4-Totais')
        menu = input('>> ').upper()
        if menu == '1':
            com += 1
            entrada_pedido(com)
        elif menu == '2':
            consulta_pedido()
        elif menu == '3':
            cardapio()
        elif menu == "4":
            total()
            continue
        elif menu[0] == "S":  # encerra o programa
            print("Deseja Encerrar o sistema?")
            print("SIM       NÂO".center(55))
            per = input(">>").upper()
            if per[0] == "S":
                print("ENCERRANDO O SISTEMA".center(55))
                break
        else:
            print('OPÇÃO INVALIDA!')
            continue
    except :
        print("Escolhe uma da opções do menu")




