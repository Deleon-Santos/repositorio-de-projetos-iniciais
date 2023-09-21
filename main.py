

def cachorro_peso():
    print('----------------------------------------Qual e o Peso do Cachorro------------------------------------------')
    cont=0
    while True:
        try:
            base = int(input('Informe o Peso do cachorro (kg): '))
            if base < 3:
                cont=40
                return
            if base >= 3 and base <10:

                return 50.00
            if base >= 10 and base <30:

                return 60.00
            if base >= 30 and base <50:

                return 70.00
            else:
                print('Nao aceitamos cochorros tao grande') #quantidade diferente da comercializada
                print('Informe o peso  do cachorro novamente')
                continue
        except ValueErro: #tratamentodoerro"informe o erro"
            print("digite um valor numerico valido")



def pelo_cao():
    print('------------------------------------------Qual o Tipo de Pelo --------------------------------------------')
    pelo_c=0
    while True:
        pelo = input('Informe o pelo do cachorro: +\n'
                             'c-curto\n'+
                             'm-medio\n'+
                             'l-longo\n'+
                           '>>')              #entre co a variavel em string
        pelo = pelo.lower()                                                 #o comando "lower" trata "str" como minusculo
        pelo = pelo.strip()                                                 #o comando "strip" trata "str" como espacos em branco
                                                                              #verificaçãode parametros
        if pelo =='c':
            pelo_c=40.00
            return
        elif pelo =='m':
            pelo_c =1.5
            return
        elif pelo =='l':
            pelo_c =2.0
            return                                                       #retorno de valores conforme a escolha
        else:                                                                  #caso nao tenha opcoes validas
            print("escolha entre as opcoes (c)/(m)/(s): ")
            continue
        #retorna ao inicio da seleção




def adicional_extra():
    print('------------------------------------------Adicionais Extras------------------------------------------------')
    contador = 0                                                                #o return do acompanhamento deve somar ao contador
    while True:
        adicional = input('deseja receber mais um adicional:\n'+
                             '1-Corte de Unhas\n'+
                             '2-Escovar os Dentes\n'+
                             '3-Limpar as Orelhas \n'+
                             '0-Nao desejo mais   nada\n'+
                            '>>')
        if adicional == '0':                                                 #digitado'0'o pedido se encerre
            return contador

        elif adicional == '1':
            contador = contador + 10
            continue                      #continue as opcoe de acompanhamento com valor(1,2,3 e 4
        elif adicional == '2':
            contador = contador + 12
            continue
        elif adicional == '3':
            contador = contador + 15
            continue
        else:
            print('Escolha uma das opcoes: (0/1/2/3')
            continue #se valor fordifrente de do menu esta messagemsera exibida






print('-----------------------------Bem-Vindo ao Pet Shop do Deleon Da Paixao Santos----------------------------------')
base = cachorro_peso()
print(base)
multiplicador = pelo_cao()
print(multiplicador)
extra = adicional_extra()
print(extra)






