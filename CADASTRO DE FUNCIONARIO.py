# CRIE UM ALGORITMO QUE LEIA INFORMAÇÕES BASICAS DE UMA PESSOA E EXIBA EM UM INICO PRINT,
# O SISTEMA DEVE CONTER AO MENOS 5 VARIAVEIS, ESTRUTURA DE DECISAO E TRATAMENTO DE ERROS.

# sistema para inserir informações
while True:
    try:

        nome = input("Inserir um nome: ")  # input de nome
        nome = nome.upper()  # metodo de tratamento
        t = len(nome)
        if t > 3:  # validação
            nome = nome
        else:
            print('Digite um nome com mais de 3 caracteres para continuar')
            continue
        while True:
            estado_civil = input(
                'Estado civil: solteiro "s"casado "c"\n' +  # input, validação e tatamento de erros em estado civil
                '>>')
            estado_civil = estado_civil.lower()
            if estado_civil == 's':
                estado_civil = 'SOLTEIRO'
                break
            elif estado_civil == 'c':
                estado_civil = 'CASADO'
                break
            else:
                print('Defina um estado civil "s" ou "c"')
                continue
        while True:
            try:
                idade = int(input('Qual a idade:'))
                if idade > 0 and idade < 150:  # validação da idade
                    idade = idade
                    break
                else:
                    print('Nao podemos considerar esta idade como valida')
                    continue
            except ValueError:
                print("Digite um valor numerico")

        while True:
            sexo_cadastro = input('Sexo : "f" ou "m"\n' +
                                  '>>')
            sexo_cadastro = sexo_cadastro.lower()  # memtodo par tratar strings meiusculas no input
            if sexo_cadastro != 'm' and sexo_cadastro != "f":
                print('Defina o sexo para cadastro: "f" ou "m"')
                continue
            if sexo_cadastro == 'm':
                sexo = 'MASCULINO'
                break
            else:
                sexo = 'FEMININO'
                break
        while True:
            try:
                salario = float(input('Digite o salario R$ '))  # input e tratamento da variavel do tipo float
                if salario > 0:
                    salario = salario
                    break
                else:
                    print('Digite um salario valido')
                    continue
            except ValueError:
                print("Digite um valor numerico")

        print(
            'Foi cadastrado um novo colaborador que se chama {},ele é {} do sexo {}, com idade {} anos e seu salario sera R$ {:.2f}'.format(
                nome, estado_civil, sexo, idade, salario))
        break
    except ValueError:
        print('Digite um valor numerico')  # tratamento de erro em caso de valores nao numerico para idade e salario
        continue