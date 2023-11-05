#inicio
import PySimpleGUI as sg
lista_saque=[]
lista_saque=[]
lista1=[]
banco_dados=[ {"cartao":"1","nome":"filho","senha":"1","saldo":20000.0},
          {"cartao":"2","nome":"pai","senha":"2","saldo":10000},
          {"cartao":"3","nome":"mae","senha":"3","saldo":50000}
          ]
# WIN_W=50
# WIN_H=80


def senha():
    x=0
    while x<3:
        #print("-" * 64)
        sen = sg.popup_get_text('Informe a Senha',font=("Any",10))
        if not sen:
            sg.popup_error()
            x+=1
            continue
        elif sen==lista1[2]:
            return True
        else:
            sg.popup("Senha incorreta")
            x += 1
            continue
def saque():
    while True:
        try:
            valor_s =int(sg.popup_get_text('Digite o VALOR'))
            if not valor_s:
                sg.popup("Infomorme um valor numerico")
                break
            elif valor_s <= lista1[3]:
                resposta=senha()
                if resposta == True:
                    sg.popup("RETIRE O VALOR NO LOCAL DETERMINADO")
                    lista1[3]=(lista1[3]-valor_s)
                    lista_saque.append(valor_s)
                    return valor_s
            #+sum(lista_saque)
            else:
                sg.popup("Saldo insuficiente")
                break

        except ValueError: #\\tratamento de erros de valores não numericos
            sg.popup("Infomorme um valor numerico")
            continue

def rest(titular):
    rest=lista1[3]
    sg.Text(rest)
    for cliente in banco_dados:
        if cliente["nome"]==titular:
            cliente.update({"saldo":rest})
            sg.Text(f"{cliente['saldo']}")
    lista1.clear()

def extrato():

    layout = [
        [sg.Text("",size=(10,1)),sg.Text("EXTRATO SIMPLIS")],
        [sg.Multiline(size=(40, 10),key="saidas")],
        [sg.Button("SAIR")],
    ]

    window = sg.Window("EXTRATO",layout,finalize=True)
    for saque in lista_saque:
        window["box"].print(*lista_saque)
        window["box"].print(*lista1)
        window["box"].print(*banco_dados)
    # for lanche in dic:
    #     layout.append([sg.Text(lanche['cod'], size=(30, 1)), sg.Text(lanche['lanche'], size=(30, 1)),
    #                    sg.Text(f'R$ {lanche["preco"]:.2f}', size=(7, 1))])
    while True:

        event, values = window.read()

        if event in (sg.WIN_CLOSED,"SAIR"):
            break

    window.close()

layout = [

    [sg.Text("OFFLINE",size=(20,1),key='nome',font=("Any", 15))],
    [sg.Text("SEJA BEM-VINDO",size=(28,1),key='output',font=("Any", 10))],
[sg.Multiline(key="box",size=(41,5))],
    [sg.Button('SALDO', size=(37, 1))],
    [sg.Button('SAQUE', size=(37, 1))],
    [sg.Button('EXTRATO', size=(37, 1))],
    [sg.Button('DEPOSITO', size=(37, 1))],
    [sg.Button('SAIR', size=(8, 1))],
    [sg.Text(size=(25,1),key='valores',font=("Any", 15))],
    #[sg.Image("morto de fome.png", size=(300, 80))],
]


window = sg.Window("CONTA CORRENTE",  layout,resizable=True)
while True:

    event, values = window.read()
    window['nome'].update("OFFLINE")
    window["output"].update("SELECIONE UMA OPERAÇÂO")
    if event in (sg.WIN_CLOSED,"SAIR"):
        break

    elif event== "SALDO" or event== "SAQUE" or event== "EXTRATO" or event=="DEPOSITO":
        cartao = sg.popup_get_text('Informe o Cartão',font=("Any",10))

        if not cartao:
            sg.popup_error()
            continue

        for cliente in banco_dados:
            if cliente['cartao'] in cartao:#\\valida se o cartão e senha digitados são igais ao banco de dados "cliente"
                titular=cliente["nome"].upper()
                lista1.append(cartao)
                lista1.append(titular)
                lista1.append(cliente["senha"])
                lista1.append(cliente["saldo"])

    while True:
        window['nome'].update(f'{lista1[1]}')
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "SAIR"):
            rest(titular)
            window['nome'].update("OFFLINE")
            window['output'].update("SEJA BEM-VINDO")
            #window['valores'].update("")
            window['box'].update("")

            break

        elif event == "SALDO":
            #window['box'].update("")
            window['box'].print(f"SALDO EM CONTA CORRENTE ")
            resposta = senha()
            if resposta== True:
                window['box'].print(f"SEU SALDO É R$ {lista1[3]:.2f}".rjust(20))

        elif event == "SAQUE":
            #window['box'].update("")
            window['box'].update(f"SAQUE EM CONTA CORRENTE ")
            resposta = saque()
            window['box'].print(f" Irforme o valor R$ {resposta:.2f} ")
            window['box'].print(f" AUTORIZADO R$ {resposta:.2f} ")

        elif event == "EXTRATO":
            window['output'].update(f"EXTRATO EM CONTA CORRENTE ")
            resposta = extrato()

        elif event == "DEPOSITO":
            resposta = senha()
            window['output'].update(f"DEPOSITO EM CONTA CORRENTE ")

            # else:
            #     sg.popup_error()

        #window['nome'].update(f'{titular}')


         #nom = input("Digite aqui a sua senha______________________________________>>")




#

window.close()