
# CONSTRUA UM SISTEMA DE RETIRADA DE VALORES SEMELHANTE AO CAIXA ELETRONICO
# FORNEÇA MECANISMOS PARA VALIDADAR ACESSO COM LOGIN E SENHAS
# VERIFIQUE SE HA SALDO DISPONIVEL EM CADA RETIRADA DE ACORDO COM CADA CLIENTE
# PERMITA QUE VISUALIZEM O SALDO
# E AO TERMINAR CADA OPERAÇAO APRESETE OS VALORES MOVIMENTADOS

#\\*******************************Inicio****************************************
#\\sistema de retirada de valores em caixa eletronico
lista_saque=[]
banco_dados=[ {"cartao":"1","nome":"filho","senha":"1","saldo":20000.0},
          {"cartao":"2","nome":"pai","senha":"2","saldo":10000},
          {"cartao":"3","nome":"mae","senha":"3","saldo":50000}
          ]


#*************************Inicio da função Saldo*******************************
def saldo_conta(saldo):
    print("-" * 64)
    print("SALDO EM CONTA CORRENTE".center(64))
    saldo -= sum(lista_saque)#\\ o saldo sera sempre a soma de soma de lista_saque - o saldo em "banco de dados
    print(f"Seu saldo em conta corrente é R$ {saldo:.2f}")
#\\Fim Saldo


#*************************Inicio da função Saque*******************************
def saque_conta(saldo):
    print("-"*64)
    print("SAQUE EM CONTA CORRENTE".center(64))
    while True:
        try:
            valor_s = float(input("Digite o valor do saque R$ "))
            if valor_s+sum(lista_saque) <=saldo:
                lista_saque.append(valor_s)
                print()
                print("SAQUE AUTORIZADO".rjust(64))
                print(f"Retire o valor no local informado R$ {valor_s:.2f}")
                break #\\ se o valor da soma for inferior a saldo do cliente a operação e aprovada

            else:
                print()
                print("SAQUE NÃO AUTORIZADO".rjust(64))
                print('Consulte saldo em conta corrente\n')
                break #\\se a soma for superior a operação sera negada

        except ValueError: #\\tratamento de erros de valores não numericos
            print("Esta transação deve ser feita com numeros\n")
            continue
#\\Fim Saque...


#*************************Inicio da função sair*******************************
def sair(titular,saldo,cartao):
    print("-"*64)
    print(f"{titular}".rjust(64))
    print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS".center(64))
    saldo_restante = saldo - sum(lista_saque)            #\\novo saldo apos os saques

    #\\bloco com irformações das retiradas
    print(f"\n>> A quantidade total de saques {len(lista_saque)}")
    print(f">> O valor total do(s) saque(s) R$ {sum(lista_saque):.2f}")
    print(f">> O saldo desta conta é R$ {saldo_restante:.2f}")
    print("\nVeja o historico de saques:")
    print(*lista_saque,sep="/")

    for cliente in banco_dados:                    #\\atualiza a chave "saldo" com os valores atuais em cliente
      if cliente["cartao"] == cartao:
          cliente.update({"saldo":saldo_restante}) #\\ atualização do saldo do cliente no banco de dados
    lista_saque.clear()                            #\\ lista a lista para não interferir em outras transações

    print()
    print("OPERAÇÃO ENCERRADA".center(64))
    print('\n*'*3)
#\\ Fim Sair


#**************************Inicio do menu de tutulos***************************
def menu(titular,senha1,saldo,cartao):
    while True:
        print()                     #\\inicio do menu de operações
        print("-"*64)
        print(f"{titular}".rjust(64))
        print("BEM-VINDO A SUA CONTA".center(64))
        menu=input("Escolha uma operação:\n"+
                  "1----------------------------------------------------------Saldo\n"+
                  "2----------------------------------------------------------Saque\n"+
                  "0-----------------------------------------------------------Sair\n"+
                  ">>")

        if menu == "1":
            saldo_l=saldo_conta(saldo)
            continue

        elif menu == "2":
            saque_l=saque_conta(saldo)
            continue

        elif menu == "0":
            encerrar = sair(titular,saldo,cartao)#\\as valiaveis são mandadas com parametros sempre que necessarias
            break

        else:
            print("Escolha uma opção do menu")
            continue
#\\Fim Menu...


def leia_me():

  print("\n                           HELP!!!\n"+
            'Este sistema foi desenvolvido em carater educativo, a validação\n'+
            'de login  e senha foram simplificados para tornar a experiencia\n'+
            'mais intuitiva e dinâmica, soluções como banco de dados externo\n'+
            'estão e interface grafica ainda serão implementados\n'+
            'Versao: 1.00.1')
  print("Dados".center(64))
  print('+--------------------------------------------------------------+')
  print('| num_cartão | senha_cartão | titular_cartão  |  saldo_titular |')
  print('+--------------------------------------------------------------+')
  print("|     1              1             filho         R$ 20.000,00  |")
  print("|     2              2              pai          R$ 10.000,00  |")
  print("|     3              3              mãe          R$ 50.000,00  |")
  print('+--------------------------------------------------------------+')
  print("ATENÇÃO!   Digite 'S' no input de cartão para encerrar o sistema")
#Fim help


#inicio
print("INICIALIZANDO O SISTEMA".center(64))

enter=input("Para acessar dados do cartão e senha do titular digite 'leia-me'\n"+
           "Digite qualquer tecla para continuar__________________>>").lower()
if enter == "leia-me":
    leia_me = leia_me()


print()
print("INICIO DE SAQUE EM CAIXA ELETRÔNICO".center(64))
print("-"*64)


while True:
    cartao = input("Digite aqui o numero do seu cartão___________________________>>").upper()#trata as letras minusculas
    if cartao[0] == "S":                    #\\ encerra se a primeira letra for "s"
        print("OPERAÇÃO ENCERRADA".center(64))
        break                               #\\encerra o sistema se digitar o valor "s"

    senha1 = input("Digite aqui a sua senha______________________________________>>")
    for cliente in banco_dados:
        if cliente['cartao'] == cartao and cliente["senha"]== senha1:#\\valida se o cartão e senha digitados são igais ao banco de dados "cliente"
            saldo = cliente["saldo"]
            titular = cliente["nome"].upper()

            menu_iniciar = menu(titular, senha1, saldo, cartao) #\\os valores de nome e saldo sao baixados para menu de operações
            continue
    print()
    print('INFORME UM CARTÃO E SENHA VALIDOS PARA CONTINUAR'.center(64))#\\retorna a pergunta ate validar acesso ou "s"para sair
#\\Fim Se...