import PySimpleGUI as sg
lista = []
#num=0
layout =[
        [sg.Text(" ",key='num')],
        [sg.Text('Descição do material')],
        [sg.Input(key='material')],#a chave recebe o material
        [sg.Text('Quantidade do material')],
        [sg.Input(key='quantidade')],
        [sg.Text('Valor do material')],
        [sg.Input(key='valor')],
        [sg.Button('        Incluir       '),sg.Button('     Concluir     '),sg.Button('     Encerrar     ')],
        [sg.Text('',key='msn')]
]

janela = sg.Window("CADASTRO DE MATERIAIS",layout)

while True:
        acao,valores = janela.read()
        if acao == sg.WIN_CLOSED:
                break
        elif acao == "Incluir":

                #num=1
                janela['num'].update(f"novo cadastro ")

                        #cadastro['numero'] = num
                        #cadastro['material'] = valores['material'].upper()
                        #cadastro['quantidade'] = valores['quantidade']
                        #cadastro['preco'] = valores['valor']
                        #print(cadastro)

                        ###beak

        if acao == "Concluir":

                janela['msn'].update(layout)
janela.close()