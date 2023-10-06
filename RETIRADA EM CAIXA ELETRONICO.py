from ast import Continue

# CONSTRUA UM SISTEMA DE RETIRADA DE VALORES SEMELHANTE AO CAIXA ELETRONICO,
# FORNEÇA MECANISMOS PARA VALIDADAR LOGIN E SENHAS
# VERIFIQUE SE HA SALDO DISPONIVEL EM CADA RETIRADA
# PERMITA QUE VISUALIZEM O SALDO
# E AO TERMINAR APRESETE OS VALORES MOVOMENTADOS

lista_saque = []
cliente = [{"num": "1", "nome": "deleon", "senha": "1", "saldo": 20000.0},
           {"num": "2", "nome": "fabio", "senha": "2", "saldo": 10000},
           {"num": "3", "nome": "antonio", "senha": "3", "saldo": 50000}
           ]


# *************************Inicio da função Saldo*******************************
def saldo_conta(saldo):
    print(">>" * 20)
    print("***SALDO EM CONTA CORRENTE***")
    t = sum(lista_saque)
    saldo -= t
    print(f"Seu saldo em conta corrente e R${saldo:.2f}")
    print()


# *************************Inicio da função Saque*******************************
def saque_conta(saldo):
    print(">>" * 20)
    print("***SAQUE EM CONTA CORRENTE***")
    while True:
        try:
            valor_s = float(input("Digite o valor do saque>>"))
            t = sum(lista_saque)
            t += valor_s

            if t <= saldo:
                lista_saque.append(valor_s)
                print()
                print(f"***SAQUE AUTORIZADO R$ {valor_s:.2f}***\n" +
                      "Retire o valor no local informado")
                break

            else:
                print()
                print("***SAQUE NÃO AUTORIZADO***\n" +
                      'Consulte saldo em conta corrente')
                break

        except ValueError:
            print("Esta transação deve ser feita com numeros")
            print()
            continue


def total(titular, saldo):
    while True:
        print(">>" * 20)
        print(f"\n***Ola, {titular}! Bem - Vindo a sua conta!***")
        menu = input(f"\nEscolha uma operação:\n" +
                     "1-saldo\n" +
                     "2-saque\n" +
                     "0-sai\n" +
                     ">>")

        if menu == "1":
            saldo_l = saldo_conta(saldo)
            continue

        elif menu == "2":
            saque_l = saque_conta(saldo)
            print(saque_l)
            continue

        elif menu == "0":
            print(">>" * 20)
            print(f"\n{titular} Obrigado por ultilizar nossos serviços")
            t = sum(lista_saque)
            l = len(lista_saque)
            t2 = saldo - t
            print(f"\nVocê realizou o total de {l} saque(s) no valor total R$ {t:.2f}")
            print(f">>O saldo desta conta é R$ {t2:.2f}")
            print("\nVeja o historico de saques")
            print(lista_saque)
            print()
            print("***OPERAÇÃO ENCERRADA!***")
            break
        else:
            print("Escolha uma opção do menu")
            continue


# *********************Inicio do Programa Principal*****************************
while True:
    cartao = input("\nDigite aqui o numero do seu cartão, ou 'S'sair >> ").upper()[0]
    if cartao[0] == "S":
        print("***OPERAÇÃO ENCERRADA!***")
        break

    senha1 = input("Digite aqui a sua senha >> ")
    for c in cliente:
        if c['num'] != cartao or c["senha"] != senha1:
            # print('***Usuario ou senha não encontrado!***')
            continue
        else:
            saldo = c["saldo"]
            titular = c["nome"].upper()
            senha = c["senha"]

            menu = total(titular, saldo)
            print(menu)
            break
    print('***Usuario ou senha não encontrado!***')
    continue







