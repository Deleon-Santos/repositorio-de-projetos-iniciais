# CONSTRUA UM SISTEMA DE RETIRADA DE VALORES SEMELHANTE AO CAIXA ELETRONICO,
# FORNEÇA MECANISMOS PARA VALIDADAR LOGIN E SENHAS
# VERIFIQUE SE HA SALDO DISPONIVEL EM CADA RETIRADA
# PERMITA QUE VISUALIZEM O SALDO
# E AO TERMINAR APRESETE OS VALORES MOVOMENTADOS
lista_saque=[]
saldo=float(20000)
num_Cartao ="1"
num_Senha ="1"
cliente=["1";"deleon";"1",]
def saldo_conta(saldo):
    print(">>" * 20)
    print("Saldo em conta corrente")
    t = sum(lista_saque)
    saldo-=t
    print(f"Seu saldo em conta corrente e R${saldo:.2f}")


def saque_conta(saldo):
    print(">>"*20)
    print("\nSaque em conta corrente")
    while True:
        try:
            valor_s = float(input("Digite o valor do saque>>"))
            t=sum(lista_saque)
            t += valor_s
            if t <=saldo:
                lista_saque.append(valor_s)
                print(f"***SAQUE AUTORIZADO R$ {valor_s:.2f}***\n" +
                      "Retire o valor no local informado")
                break
            else:
                print("***SAQUE NÃO AUTORIZADO***\n"+
                      'Consulte saldo em conta corrente')
                break
        except ValueError:
            print("Esta transação deve ser feita com numeros")
            continue



#inicio do programa principal
while True:
    cartao = input("Digite aqui o numero do seu cartão>>")
    if cartao!=num_Cartao:
        print("Cartão invalido")
        continue
    else:
        while True:
            senha=input("Informe a sua senha>>")
            if senha != num_Senha:
                print("Senha invalida")
                continue
            else:
                while True:
                    print(">>"*20)
                    menu=input("\nBem - Vindo a sua conta! O que voce deseja fazer?\n"+
                               "1-saldo\n"+
                               "2-saque\n"+
                               "0-sai\n"+
                               ">>")
                    if menu == "1":
                        saldo_l=saldo_conta(saldo)

                        continue
                    elif menu == "2":
                        saque_l=saque_conta(saldo)
                        print(saque_l)

                        continue
                    elif menu == "0":
                        print(">>"*20)
                        print("\nObrigado po ultilizar nossos serviços")
                        t = sum(lista_saque)
                        l=len(lista_saque)
                        t2=saldo-t
                        print(f">>Voce realizou o total de {l} saque(s) no valor total R$ {t:.2f}")
                        print(f">>O saldo desta conta é R$ {t2:.2f}")
                        print("veja o historico de saques")
                        print(lista_saque)
                        print("***OPERAÇÃO ENCERRADA!***")
                        break

                    else:
                        print("Escolha uma opção do menu")
                        continue
                    break
            break
        break
    break


