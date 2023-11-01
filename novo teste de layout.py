import PySimpleGUI as sg

lista_produto = []
lista1 = []
com =int(0)
cancela = []
soma2 = 0
num = int(0)

menu_layout=[["Novo",["Nova Compra","Novo Produto","Pesquisar Produto"]],
             ["Totais",["Venda Cupom","Venda Total"]],["Suporte",["Ajuda","Data"]]]
layout = [
    [sg.Menu(menu_layout)],
    [],
    [sg.Text("CAIXA ABERTO", size=(24, 1), justification='right', font=("Any", 50))],
   
    [sg.Text('Quantidade do Produto',size=(25,1),font=("Any", 18)),sg.InputText("1",size=(8,1),key='qtd')],
     
    [sg.Text('Código do Produto',size=(25,1),font=("Any", 18)), sg.InputText(size=(8,1),key='lanche1'),
     sg.InputText(size=(76,1),key='descricao')],#,sg.InputText(size=(23,1),key="com",font=("Any", 25))],
    [sg.Button('OK',size=(30,1)),sg.Text("",size=(11,1)),
     sg.Button('DELETE',size=(30,1)),sg.Text("",size=(11,1)),sg.Button('PAGAR',size=(30,1)),
     sg.Text("",size=(12,1)),sg.Button('VOLTAR',size=(30,1))],
     [sg.Text("",size=(10,1),font=("Any",1))],
    [sg.Image(filename='sd.png',size=(400,390)),sg.Multiline(size=(100, 17), key='output',font=("Any", 15))],
    [sg.Text("12 de outubro de 1233",size=(25,1),key='data',font=("Any", 12)),sg.Text("OPERADOR:",size=(10,1),font=("Any", 10)),sg.Text("ADMINISTRADOR",size=(20,1),key='LOG',font=("Any", 10)),
     sg.Text("",size=(40,1)),sg.Text("SubTotal",size=(7,2),font=("Any", 40)), sg.Text("R$ 0.00",size=(10,2),key="subtotal",font=("Any", 40), justification='right')],
    
]
window = sg.Window("NOVO PEDIDO", layout,resizable=True)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED,"Fechar"):
        sg.popup("ENCERRAR")
        break
window.close()