
import PySimpleGUI as sg
import json
lista_produto = []
lista1 = []
com =int(0)
cancela = []
soma2 = 0
num = int(0)
with open('comanda.txt', 'r') as adic:
    dic = json.load(adic)

#=============================================================================================================
def remover(soma2):
    try:
        num1 =int(sg.popup_get_text('Digite o número do item'))
        sg.popup(lista1)

        for lanche in lista1:
            if lanche["Item"] == num1:
                soma2 -= lanche["Preco"]
                cancela.append(lanche["Preco"])

                sg.popup(f'N°{lanche["Item"]} {lanche["Cod"]}-{lanche["Lanche"]:<14}{lanche["Quantidade"]:<14} R$ {pre:.2f}')
                lista1.remove(lanche)

        sg.popup("REMOVIDO")
        return soma2
    except ValueError:
        sg.popup("Não encontrado")
        return soma2

#===========================================================================================================
def total():
    layout = [
        [sg.Text("VENDA TOTAL DO DIA", size=(30, 1), justification='center', font=("Any", 18))],
        [sg.Multiline(size=(60, 10), key='output')],
        [sg.Text("",size=(16,1)),sg.Text(key="qtd",font=("Any", 18)),sg.Text("",size=(9,1)), sg.Text(key="R$",font=("Any", 18))],
    ]
    window = sg.Window("Resumo de Vendas", layout, finalize=True)
    window['output'].print("     Produto                             Quantidade                            Valor")
    qtd_t = 0
    som_t = 0
    for l in dic:
        produto = l["lanche"]
        qtd = 0
        somas = 0
        for lanche in lista_produto:
            if lanche["Lanche"] == produto:
                qtd += lanche["Quantidade"]
                somas += lanche["Preco"]
        if qtd > 0:
            window['output'].print(f'{"":<2} {produto:<10}', end="    ")
            window['output'].print(f' {qtd:>30}                                R$ {somas:.2f}'.rjust(60))
            qtd_t += qtd
            som_t += somas
    window['qtd'].print(f'Qtd {qtd_t}')
    window['R$'].print(f'R$ {som_t:.2f}')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Fechar"):
            break
    window.close()

#===========================================================================================================
def achar(lanche1):
    for lanche in dic:
        if lanche["cod"] == lanche1:
            return lanche["cod"]
    sg.popup("Não Encontrado")
    return

#============================================================================================================
def novo_item():
    #egue os itens existentes do arquivo JSON
    with open("comanda.txt", 'r') as arquivo:
        dic = json.load(arquivo)

    layout = [
        [sg.Text("Cadastrar Item")],
        [sg.Text("Código:", size=(10, 1)), sg.Text("", size=(10, 1), key="codigo")],
        [sg.Text("Produto:", size=(10, 1)), sg.InputText(key="produto")],
        [sg.Text("Preço:", size=(10, 1)), sg.InputText(key="preco")],
        [sg.Button("Cadastrar"), sg.Button("Sair")],
    ]

    window = sg.Window("Cadastro de Itens", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Sair"):
            break
        elif event == "Cadastrar":
            t= len(dic) +101
            numero=str(t)
            window["codigo"].update(numero)
            prod = values["produto"]
            prec =float(values["preco"])
            cadastro_item = {"cod": numero, "lanche": prod, "preco": prec}

            # Adicione o novo item ao dicionário
            dic.append(cadastro_item)

            with open("comanda.txt", 'w') as arquivo:
                # Grave o dicionário atualizado no arquivo
                json.dump(dic, arquivo, indent=4)

            sg.popup(cadastro_item, title="Item Cadastrado")

    window.close()

#===========================================================================================================

menu_layout=[["Novo",["Nova Compra","Novo Produto","Pesquisar Produto"]],["Totais",["Venda Comanda","Venda Total"]],["Suporte",["Ajuda"]]]
layout = [
    [sg.Menu(menu_layout)],
       [sg.Text("SEJA BEM-VINDO", size=(52, 1), justification='center', font=("Any", 35)), sg.Image("morto de fome.png",size=(1,1))],
    [sg.Text('Código do lanche',size=(25,1),font=("Any", 18)), sg.InputText(size=(8,1),key='lanche1'),sg.Text(" ",size=(85,1)),sg.Text(size=(13,1),key="com",justification='right',font=("Any", 18))],
    [sg.Text('Quantidade do lanche',size=(25,1),font=("Any", 18)),sg.InputText(size=(8,1),key='qtd')],
    [sg.Button('OK',size=(30,1)),sg.Text("",size=(11,1)),
     sg.Button('DELETE',size=(30,1)),sg.Text("",size=(11,1)),sg.Button('PAGAR',size=(30,1)),
     sg.Text("",size=(12,1)),sg.Button('VOLTAR',size=(30,1))],
    [sg.Multiline(size=(150, 12), key='output',font=("Any", 24))],
    [sg.Text("",size=(108,1)), sg.Text(size=(18,1),key="subtotal",font=("Any", 35), justification='right')],
]

window = sg.Window("NOVO PEDIDO", layout,resizable=True)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED,"Fechar"):
        sg.popup("ENCERRAR")
        break
    elif event == "Nova Compra":
        com+=1
        window['com'].update(f'COMANDA N°{com}')
        while True:
            try:
                event, values = window.read()
                if event == 'OK':
                    lanche1 = values['lanche1']
                    qtd = values["qtd"]
                    if not lanche1 or not qtd:
                        sg.Text("Informe valores para continuar")
                        continue
                    else:
                        pro=achar(lanche1)
                        if pro == lanche1:
                            qtd = int(qtd)
                            for item in dic:
                                if item["cod"] == pro:
                                    num += 1


                                    lanche = item["lanche"]
                                    preco = item['preco'] * qtd
                                    soma2 += preco
                            dicionario = {'Comanda': com, 'Item': num,"Cod":pro, 'Lanche': lanche, 'Quantidade': qtd,
                                          'Preco': preco}
                            lista1.append(dicionario.copy())

                            for lanche in lista1:
                                pre = lanche["Preco"]
                            output_text = f'N°{"":<7}{lanche["Item"]} {"":>25}{lanche["Cod"]}-{lanche["Lanche"]:<18}{"":>20} {lanche["Quantidade"]:<18}{"":>18} R$ {pre:.2f}'
                            window['output'].print(output_text)
                            window['subtotal'].update(f"SubTotal R$ {soma2:.2f}")
                            continue
                        else:
                            continue
                elif event == 'DELETE':
                    soma2= remover(soma2)
                    window['subtotal'].update(f"SubTotal R$ {soma2:.2f}")
                    condicao=len(cancela)
                    if condicao==1:
                        window['output'].print(f'-R$ {cancela[0]:.2f}'.rjust(120))
                        cancela.clear()
                    continue
                elif event == 'PAGAR':
                    sg.popup(f'Pagar R${soma2:.2f}')
                    lista_produto.extend(lista1)
                    lista1.clear()
                    soma2=0
                    num=0
                    window["output"].update("")
                    window["subtotal"].update("")
                    break
                elif event == "VOLTAR":
                    lista1.clear()
                    soma2 = 0
                    num=0
                    window["com"].update("")
                    window["output"].update("")
                    window["subtotal"].update("")
                    break
                elif event == (sg.WIN_CLOSED):
                    sg.popup("ENCERRAR")
                    break
            except ValueError:
                sg.popup('Entre com um valor numérico')
                continue
    elif event == "Venda Total":
        total()
    elif event == "Pesquisar Produto":
        window["com"].update("PESQuISAR PRODUTO")
        window["output"].print(f'{"CÓDIGO" :<20}                 {"PRODUTO":<20}                            {"PRECO"}')
        for lanche in dic:
            window['output'].print(f"    {lanche['cod']:<40} {lanche['lanche']:<40} R$ {lanche['preco']:>15.2f}")
    elif event == "VOLTAR":
        window["output"].update("")
        window["com"].update("")
        continue
    elif event == "Novo Produto":
        novo_item()
    elif event == "Ajuda":
        sg.popup('o sistema de comandas ainda esta em desenvolvimento')


        continue
window.close()



#