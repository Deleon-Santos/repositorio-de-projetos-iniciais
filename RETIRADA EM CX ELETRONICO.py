
lista_saque=[]
retirada={}
saldo=float(20000)
valor=float(0)
num_Cartao ="1"
num_Senha ="1"


def saldo_conta(saldo):
    print("Saldo em conta corrente")
    print(f"Seu saldo em conta corrente e R${saldo:.2f}")
    print(lista_saque)


def saque_conta(saldo,valor):
    print("Saque em conta corrente")

    while True:

        try:
            valor_s=float(input("Digite o valor do saque"))
            valor+=valor_s
            if valor <= saldo:
                saldo-=valor_s
                retirada= {'Saques': valor_s}
                lista_saque.append(retirada.copy())
                print("SAQUE AUTORIZADO\n" +
                      "Retire o valor no local informado")
                #print(lista_saque)
                #return saldo, valor
                break
            else:
                print("SAQUE NÃO AUTORIZADO\n"+
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
                    print("Bem - Vindo a sua conta")
                    menu=input("O que voce deseja fazer?\n"+
                               "1-saldo\n"+
                               "2-saque\n"+
                               "0-sai\n"+
                               ">>")
                    if menu == "1":
                        saldo_l=saldo_conta(saldo)
                        print(saldo_l)
                    elif menu == "2":
                        saque_l=saque_conta(saldo,valor)
                        print(saque_l)
                    elif menu == "0":
                        print("Obrigado po ultilizar nossos serviços")
                        print(f"O saldo desta conta é R$ {saldo}")
                        for saque in lista_saque:
                            for k, v in saque.items():
                                print(f"{k} : {v}")
                                break

                    else:
                        print("Escolha uma opção do menu")
                    break
            break
        break
    break


