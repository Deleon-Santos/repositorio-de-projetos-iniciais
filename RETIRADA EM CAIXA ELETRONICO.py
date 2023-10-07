# CONSTRUA UM SISTEMA DE RETIRADA DE VALORES SEMELHANTE AO CAIXA ELETRONICO
# FORNEÇA MECANISMOS PARA VALIDADAR ACESSO COM LOGIN E SENHAS
# VERIFIQUE SE HA SALDO DISPONIVEL EM CADA RETIRADA DE ACORDO COM CADA CLIENTE
# PERMITA QUE VISUALIZEM O SALDO
# E AO TERMINAR CADA OPERAÇAO APRESETE OS VALORES MOVIMENTADOS

# \\*******************************Inicio****************************************
# \\sistema de retirada de valores em caixa eletronico
lista_saque = []
banco_dados = [{"num": "1", "nome": "deleon", "senha": "1", "saldo": 20000.0},
               {"num": "2", "nome": "fabio", "senha": "2", "saldo": 10000},
               {"num": "3", "nome": "antonio", "senha": "3", "saldo": 50000}
               ]


# *************************Inicio da função Saldo*******************************
def saldo_conta(saldo):
    print()
    print("--" * 23)
    print("***SALDO EM CONTA CORRENTE***")
    soma = sum(lista_saque)  # \\ o saldo sera sempre a soma de soma de lista_saque - o saldo em "banco de dados
    saldo -= soma
    print(f"Seu saldo em conta corrente e R${saldo:.2f}")


# \\Fim Saldo


# *************************Inicio da função Saque*******************************
def saque_conta(saldo):
    print()
    print("--" * 23)
    print("***SAQUE EM CONTA CORRENTE***")
    while True:
        try:
            valor_s = float(input("Digite o valor do saque>>"))
            soma = sum(
                lista_saque)  # \\soma as retirados anteriores + o valor informado e compara com o saldo existente
            soma += valor_s

            if soma <= saldo:
                lista_saque.append(valor_s)
                print()
                print(f"***SAQUE AUTORIZADO R$ {valor_s:.2f}***\n" +
                      "Retire o valor no local informado")
                break  # \\ se o valor da soma for inferior a saldo do cliente a operação e aprovada

            else:
                print()
                print("***SAQUE NÃO AUTORIZADO***\n" +
                      'Consulte saldo em conta corrente\n')
                break  # \\se a soma for superior a operação sera negada

        except ValueError:  # \\tratamento de erros de valores não numericos
            print("Esta transação deve ser feita com numeros")
            print()
            continue


# \\Fim Saque...


# *************************Inicio da função sair*******************************
def sair(titular, saldo, cartao):
    print()
    print("--" * 23)
    print(f"{titular} Obrigado por ultilizar nossos serviços")
    soma = sum(lista_saque)  # \\soma do valores da lista "lista_saques"
    qtd = len(lista_saque)  # \\soma dos saques realizados durante a operação
    saldo_restante = saldo - soma  # \\novo saldo apos os saques

    # \\bloco com irformações das retiradas
    print(f"\nVocê realizou o total de {qtd} saque(s) no valor total R$ {soma:.2f}")
    print(f">>O saldo desta conta é R$ {saldo_restante:.2f}")
    print("\nVeja o historico de saques")
    print(lista_saque)

    for cliente in banco_dados:  # \\atualiza a chave "saldo" com os valores atuais em cliente
        if cliente["num"] == cartao:
            cliente.update({"saldo": saldo_restante})  # \\atualização
    lista_saque.clear()  # \\ lista a lista para não interferir em outras transações

    print()
    print("***OPERAÇÃO ENCERRADA!***")
    print('\n*' * 3)


# \\ Fim Sair


# **************************Inicio do menu de tutulos***************************
def menu(titular, saldo, cartao):
    while True:
        print()  # \\inicio do menu de operações
        print("--" * 23)
        print(f"***Ola, {titular}! Bem - Vindo a sua conta!***")
        menu = input(f"\nEscolha uma operação:\n" +
                     "1-Saldo\n" +
                     "2-Saque\n" +
                     "0-Sar\n" +
                     ">>")

        if menu == "1":
            saldo_l = saldo_conta(saldo)
            continue

        elif menu == "2":
            saque_l = saque_conta(saldo)
            continue

        elif menu == "0":
            encerrar = sair(titular, saldo, cartao)  # \\as valiaveis são mandadas com parametros sempre que necessarias
            break

        else:
            print("Escolha uma opção do menu")
            continue


# \\Fim Menu...


# *********************Inicio do Programa Principal*****************************
while True:
    cartao = input("\nDigite aqui o numero do seu cartão ou 'S'sair >> ").upper()  # trata as letras minusculas
    if cartao[0] == "S":  # encerra se a primeira letra for "s"
        print("***OPERAÇÃO ENCERRADA!***")
        break  # \\encerra o sistema se digitar o valor "s"

    senha1 = input("Digite aqui a sua senha >> ")
    for cliente in banco_dados:
        if cliente['num'] == cartao and cliente[
            "senha"] == senha1:  # \\valida se o cartão e senha digitados são igais ao banco de dados "cliente"
            saldo = cliente["saldo"]
            titular = cliente["nome"].upper()

            escolha = menu(titular, saldo, cartao)  # \\os valores de nome e saldo sao baixados para menu de operações

    print(
        '\nINFORME UM CARTÃO E SENHA VALIDOS PARA CONTINUAR')  # \\retorna a pergunta ate validar acesso ou "s"para sair
# \\Fim Se...




