
#RESOLVENDO O EXERCICIO 3 DE LOGICA DE PROGRAMAÇÃO E ALGORITIMO
#inicio da finção cachorro peso
def cachorro_peso():
    print('----------------------------------------Qual e o Peso do Cachorro------------------------------------------')

    while True: #inicio de laço
        try: #testar e tratar possiveis erros
            base = int(input('Informe o Peso do cachorro (kg): '))
            if base < 3: # retorna os vaores de acordo com o input de peso
                return 40
            elif base >= 3 and base <10:
                return 50.00
            elif base >= 10 and base <30:
                return 60.00
            elif base >= 30 and base <50:
                return 70.00
            else:
                print('Nao aceitamos cochorros tao grande') #quantidade diferente da comercializada
                print('Informe o peso  do cachorro novamente')
                continue #retorna ao inicio do laço de repetição
        except ValueError: #tratamento do erro de valores não numerico
            print("digite um valor numerico valido")


#inicio da função cachorro pelo
def cachorro_pelo():
    print('------------------------------------------Qual o Tipo de Pelo ---------------------------------------------')

    while True:
        pelo = input('Informe o pelo do cachorro: +\n'
                             'c-curto\n'+
                             'm-medio\n'+
                             'l-longo\n'+
                           '>>') #entre co a variavel em string
        pelo = pelo.lower() #o comando "lower" trata "str" como minusculo
        pelo = pelo.strip() #o comando "strip" trata "str" como espacos em branco

        if pelo =='c':
            return 1
        elif pelo =='m':
            return 1.5
        elif pelo =='l':
            return 2.0   #retorno de valores conforme a escolha
        else: #caso nao tenha opcoes validas
            print("escolha entre as opcoes (c)/(m)/(s): ")
            continue #retorna ao inicio do laço



#inicio da função adicional extra
def adicional_extra():
    print('------------------------------------------Adicionais Extras------------------------------------------------')
    contador = 0 #o return do acompanhamento deve somar ao contador
    while True: #o laço de repetição vai oferecer novas opções ate "0"
        adicional = input('deseja receber mais um adicional:\n'+
                             '1-Corte de Unhas\n'+
                             '2-Escovar os Dentes\n'+
                             '3-Limpar as Orelhas \n'+
                             '0-Nao desejo mais   nada\n'+
                            '>>')
        if adicional == '0': #digitado'0'o pedido se encerre
            return contador
        elif adicional == '1':
            contador = contador + 10
            continue        #continue as opcoe de acompanhamento com valor(1,2,3 e 4
        elif adicional == '2':
            contador = contador + 12
            continue
        elif adicional == '3':
            contador = contador + 15
            continue
        else:
            print('Escolha uma das opcoes: (0/1/2/3') #se valor for difrente do menu, esta messagem sera exibida
            continue



#inicio do programa principal
print('--------------------------------------Bem-Vindo ao PetShop do Deleon ME ---------------------------------------')
base = cachorro_peso()

multiplicador = cachorro_pelo()

extra = adicional_extra()

total=base*multiplicador+extra
print(f"O peso do seu cachorro è R$ {base:.2f} foi multiplicado tamanho do pelo no multiplicador {multiplicador} e os adicionais somam R$ {(extra):.2f}")
print(f"Seu gasto total foi R$ {(total):.2f}")
#Final do programa principal






