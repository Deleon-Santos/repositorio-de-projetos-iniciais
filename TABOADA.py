import PySimpleGUI as sg
data=[]
sg.theme("DarkBlue1")

visor  =[[sg.Input("0", size=(18, 1), font=("Any", 30, "bold"), key="out", justification='right')],]

numeros=[[sg.Button("7", size=(7,3), key="7", font="bold"), sg.Button("8", size=(7, 3), key="8", font="bold"), sg.Button("9", size=(7, 3), key="9", font="bold")],
        [sg.Button("4", size=(7, 3), key="4", font="bold"), sg.Button("5", size=(7, 3), key="5", font="bold"), sg.Button("6", size=(7, 3), key="6", font="bold")],
        [sg.Button("1", size=(7, 3), key="1", font="bold"), sg.Button("2", size=(7, 3), key="2", font="bold"), sg.Button("3", size=(7, 3), key="3", font="bold")],
        [sg.Button("+/-", size=(7, 3), key="+/-", font="bold"), sg.Button("0", size=(7, 3), key="0", font="bold"), sg.Button(",", size=(7, 3), key=".", font="bold")],]
    

bloco1 =[[sg.Button("<", size=(6, 3), font="bold", key="<")],
        [sg.Button("x", size=(6, 3), font="bold", key="*")],
        [sg.Button("-", size=(6, 3), font="bold", key="-")],
        [sg.Button("+", size=(6, 3), font="bold", key="+")],]

bloco2 =[[sg.Button("C", size=(7, 3), font="bold", key="c")],
        [sg.Button("/", size=(7, 3), font="bold", key="/")],
        [sg.Button("%", size=(7, 3), font="bold", key="%")],
        [sg.Button("=", size=(7, 3), font="bold", key="=")],]
    

layout_calculadora =[[sg.Frame("", visor)],
                     [sg.Frame("", numeros), sg.Col(bloco1), sg.Col(bloco2)],
                     [sg.Radio("Média", "RADIO1", size=(9, 1), key="m"),
                      sg.Radio("Raíz", "RADIO1", size=(9, 1), key="r"),
                      sg.Radio("Potência", "RADIO1", size=(9, 1), key="po"),
                      sg.Radio("IMC", "RADIO1", size=(9, 1), key="imc")
                      ],]
#//////////////////////////////////////////////////////////////////////////////   
c1 = [
    [sg.Radio("Adição", "RADIO", default=True, size=(8, 1), key="somar"), sg.Radio("Subtração", "RADIO", size=(8, 1), key="diminuir"),
     sg.Radio("Multiplicação", "RADIO", size=(9, 1), key="multiplicar"), sg.Radio("Divisão", "RADIO", size=(5, 1), key="dividir")],
    [sg.Text("Vamos conhecer taboada do Numero:", font=("Verdana", 11)),
     sg.Spin(values=[i for i in range(1, 10)], initial_value=1, key='spin', size=(1, 1), font=("Verdana", 11)),
     sg.Button("OK", size=(5, 1))],
    [sg.Image(filename="image 2.png", size=(230, 310)), sg.Table(values= data, headings=["N1", "Op", "N2","Op2","Resp"], auto_size_columns=True, justification='right',size=(12,18) ,key='-OUT-')],
    [sg.Button("Clear")],
]
c2 = [[sg.Image(filename="taboada.png", size=(230, 409))], ]

va1 = [[sg.Frame("", c1)],]
col =[[sg.Col(va1)],]

tab_layout2 = [[sg.Frame("",layout_calculadora)], ]
tab_layout1 = [[sg.Frame("",col)], ]

menu_botao = [["Opções", ["Raiz Quandrada", "Potência", "Percentual", "Média"]], ["Ajuda", ["Ajuda", "Sobre"]]]
janela = [
    [sg.MenuBar(menu_botao)],
    [sg.Text("NOVA TABOADA", size=(45, 1), justification='center', font=("Any", 18, "bold"), relief='flat')],
    [sg.TabGroup([
    [sg.Tab("                    Taboada                     ", tab_layout1), 
     sg.Tab("                  Calculadora                  ", tab_layout2,key="calcular")],]),
    sg.Image(filename="taboada.png", size=(230, 460))],
    [sg.Button("Sair",size=(12,1))],
    ]


window = sg.Window("TABOADA", janela, resizable=True)
operadores = ["+", "-", "*","/"]


    ##----CALCULATOR FUNCTIONS-------------------------------##
var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

#-----HELPER FUNCTIONS
def format_number() -> float:
    ''' Create a consolidated string of numbers from front and back lists '''
    return float(''.join(var['front']).replace(',','') + '.' + ''.join(var['back']))


def update_display(display_value: str):
    ''' Update the calculator display after an event click '''
    try:
        window["out"].update(value='{:,.2f}'.format(display_value))
    except:
        window['out'].update(value=display_value)


#-----CLICK EVENTS
def number_click(event: str):
    ''' Number button button click event '''
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())


def clear_click():
    ''' CE or C button click event '''
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False


def operator_click(event: str):
    ''' + - / * button click event '''
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()


def calculate_click():
    ''' Equals button click event '''
    global var
    try:
        var['y_val'] = format_number()
    except ValueError: # When Equals is pressed without any input
        var['x_val'] = var['result']
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()
    except:
        update_display("ERROR! DIV/0")
        clear_click()


while True:
    numeros = [str(i)for i in range(0, 10)] #uma laço para gerar "0 a 9 convertidos em str
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Sair"):
        break

    if event == "OK":
        numero = int(values["spin"])

        if values["somar"] == True:
            data.append(["", ""," ", "", ""])
            data.append(["==", "==","==", "==", "===="])
            for fator in range(1, 11):
                data.append([numero, "+", fator, "=", numero + fator])
            data.append(["==","==","==", "==", "===="])
            window["-OUT-"].update(values=data)

        elif values["diminuir"] == True:
            data.append(["", ""," ", "", ""])
            data.append(["==", "==","==", "==", "===="])
            for fator in range(1, 11):
                data.append([numero, "-", fator, "=", numero - fator])
            data.append(["==","==","==", "==", "===="])
            window["-OUT-"].update(values=data)

        elif values["multiplicar"] == True:
            data.append(["", ""," ", "", ""])
            data.append(["==", "==","==", "==", "===="])
            for fator in range(1, 11):
                data.append([numero, "x", fator, "=", numero * fator])
            data.append(["==","==","==", "==", "===="])
            window["-OUT-"].update(values=data)

        elif values["dividir"]:
            data.append(["", ""," ", "", ""])
            data.append(["==", "==","==", "==", "===="])
            for fator in range(1, 11):
                resutado=numero/fator
                resultado_formatado = "{:.1f}".format(resutado)
                data.append([numero, "/", fator, "=", resultado_formatado])
            data.append(["==","==","==", "==", "===="])
            window["-OUT-"].update(values=data)
        elif event=="Clear":
                window["-OUT-"].update("")   
   
#////////////////////////////////////////////////////////////////////////////////////////////////////////

    

#-----MAIN EVENT LOOP------------------------------------##

        if event in ['0','1','2','3','4','5','6','7','8','9']:
            number_click(event)
        if event in ['Escape:27','C','CE']: # 'Escape:27 for keyboard control
            clear_click()
            update_display(0.0)
            var['result'] = 0.0
        if event in ['+','-','*','/']:
            operator_click(event)
        if event == '=':
            calculate_click()
        if event == '.':
            var['decimal'] = True
        if event == '%':
            update_display(var['result'] / 100.0)