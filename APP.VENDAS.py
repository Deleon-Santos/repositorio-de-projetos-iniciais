
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
        for lanche in lista1:
            if lanche["Item"] == num1:
                soma2 -= lanche["Preco"]
                cancela.append(lanche["Preco"])
                sg.popup(f'N°{lanche["Item"]}                                {lanche["Cod"]}-{lanche["Lanche"]:<14}{lanche["Quantidade"]:<14} R$ {pre:.2f}')
                lista1.remove(lanche)
        
        return soma2
    except ValueError:
        sg.popup("Não encontrado")
        return soma2

#=============================================================================================================
def venda_cupom():
    layout = [
        [sg.Text("VENDA POR CUPOM", size=(50, 1), justification='center', font=("Any", 18))],
        [sg.Text("", size=(10, 1))],
        [sg.Text("N° do Cupom Fiscal",size=(20,1)),sg.InputText(key="cupom",size=(10)),sg.Text("",size=(44,1)),sg.Button("Pesquisar",size=(11,1))],
        [sg.Multiline(size=(100, 20), key='output')],
        [sg.Text("",size=(58,1)),sg.Text("Total",size=(8,1),font=("Any", 18)), sg.Text(key="R$",size=(8,1),justification='right',font=("Any", 18))],
    ]
    window = sg.Window("Resumo de Vendas", layout, finalize=True)
    window['output'].print("      Item       Produto                                                                        Quantidade                   Valor")
    while True:
        try:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Fechar"):
                break
            elif event == "Pesquisar":           
                cupom=int(values["cupom"])
                for produto in lista_produto:
                    soma=float(0)
                    if produto["Comanda"]== cupom:
                    
                        window['output'].print(f'{"":<4}  N°{lanche["Item"]:<8} {lanche["Cod"]} - {lanche["Ean"]} - {lanche["Lanche"]:<40} {lanche["Quantidade"]}') #R$ {lanche["Preco"]:.2f}')
                        window['output'].print(f'R$ {lanche["Preco"]:.2f}'.rjust(140))
                        window["output"].print("      ======================================================================")
                        soma+=lanche["Preco"]
                    window["R$"].update(f"R$ {soma:.2f}")
                sg.Text("Informe um cupom para continuar")
                continue
                
        except: 
            sg.Text("Informe um cupom para continuar")           
    window.close()

#===========================================================================================================
def total():
    layout = [
        [sg.Text("VENDA TOTAL DO DIA", size=(50, 1), justification='center', font=("Any", 18))],
        [sg.Multiline(size=(100, 20), key='output')],
        [sg.Text("",size=(56,1)),sg.Text(key="qtd",font=("Any", 18)),sg.Text("",size=(9,1)), sg.Text(key="R$",justification='center',font=("Any", 18))],
    ]
    window = sg.Window("Resumo de Vendas", layout, finalize=True)
    window['output'].print("      Produto                                                                                       Quantidade                Valor")
    qtd_t = 0
    som_t = 0
    for l in dic:
        produto = l["lanche"]
        qtd = 0
        somas = 0
        for lanche in lista_produto:
            if lanche["Lanche"] == produto:
                qtd += lanche["Quantidade"]
                cod=lanche["Cod"]
                ean=lanche["Ean"]
                somas += lanche["Preco"]
        if qtd > 0:
            window['output'].print(f'{"":<5} {cod} - {ean} - {produto:<10}{qtd:>30}')
            window['output'].print(f'                                 R$ {somas:.2f}'.rjust(140))
            window["output"].print("      ======================================================================")
            qtd_t += qtd
            som_t += somas
    window['qtd'].print(f'Qtd {qtd_t}')
    window['R$'].print(f'R$ {som_t:.2f}')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Fechar"):
            break
    window.close()


import PySimpleGUI as sg
#=====================================================================================================================
def pagar(soma2):
    layout = [
        [sg.Text("CONDIÇÃO DE PAGAMENTO", size=(35, 1), justification='center', font=("Any", 18))],
        [sg.Text("", size=(10, 1))],
        [sg.Text("Valor Total da Compra ", size=(28, 1) ,font=("Any",12)), sg.Text(f"R$ {soma2:.2f}", size=(18, 1),justification='right', key="valor", font=("Any", 18))],
        [sg.Text("Valor Recebido ", size=(28, 1), font=("Any", 12)), sg.Text(f'R$ 0.00', size=(18, 1), key="recebido",justification='right', font=("Any", 18))],
        [sg.Text("Troco Devolvido ", size=(28, 1), font=("Any", 12)), sg.Text(f'R$ 0.00', size=(18, 1), key="R$",justification='right', font=("Any", 18))],
        [sg.Text("", size=(10, 1))],
        [sg.Text("", size=(20, 1)),sg.Button('CARTAO', size=(20, 1)), sg.Button('PIX', size=(20, 1)), sg.Button('DINHEIRO', size=(20, 1))],
        #[sg.Text("",size=(20)),sg.Button('Sair', size=(20, 1))],
    ]

    window = sg.Window("PAGAMENTO", layout,finalize=True)

    while True:
        event, values = window.read()
        soma2 = soma2
        troco=0
        window["valor"].update(f"R$ {soma2:.2f}")

        if event in (sg.WIN_CLOSED, "Voltar"):
            
            break

        elif event in ("CARTAO", "PIX"):
            soma2 = 0
            
            
            sg.popup("Pagamento efetuado com sucesso")
            return soma2
        elif event=="Sair":
            return soma2
        elif event == "DINHEIRO":
            try:
                dinheiro = float(sg.popup_get_text("Valor Recebido"))
                window["recebido"].update(f"R$ {dinheiro:.2f}")
                if dinheiro >= soma2:
                    troco = dinheiro - soma2
                    window["R$"].update(f"R$ {troco:.2f}")
                    soma2 = 0
                    
                    sg.popup("Pagamento efetuado com sucesso")
                    return soma2
                    
                else:
                    sg.popup("Insira um valor maior ou escolha outra forma de pagamento")
            except ValueError:
                sg.popup("Insira um valor válido")
                continue
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
        [sg.Text("CADASTRAR ITEM", size=(35, 1), justification='center', font=("Any", 18))],
        [sg.Text("", size=(20, 1))],
        [sg.Text("Código:", size=(10, 1)), sg.Text("", size=(10, 1), key="codigo")],
        [sg.Text("Produto:", size=(10, 1)), sg.InputText(key="produto",size=(25,1),font=("Any",18))],
        [sg.Text("Preço:", size=(10, 1)), sg.InputText(key="preco",size=(25,1),font=("Any",18))],
        [sg.Text("", size=(20, 1))],
        [sg.Text("", size=(17, 1)),sg.Button("Cadastrar",size=(11, 1)), sg.Button("Sair",size=(11, 1))],
    ]

    window = sg.Window("Cadastro de Itens", layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Sair"):
            break
        elif event == "Cadastrar":
            t= len(dic) +101
            numero=str(t)
            ean=7890000000000+t
            ean=str(ean)
            window["codigo"].update(numero)
            prod = values["produto"]
            prec =float(values["preco"])
            cadastro_item = {"cod": numero,"ean":ean, "lanche": prod, "preco": prec}
            # Adicione o novo item ao dicionário
            dic.append(cadastro_item)
            with open("comanda.txt", 'w') as arquivo:
                # Grave o dicionário atualizado no arquivo
                json.dump(dic, arquivo, indent=4)
            sg.popup(cadastro_item, title="Item Cadastrado")
    window.close()

#===========================================================================================================
sg.theme("Dark Amber")


menu_layout=[["Novo",["Nova Compra","Novo Produto","Pesquisar Produto"]],
             ["Totais",["Venda Cupom","Venda Total"]],["Suporte",["Ajuda","Data"]]]
layout = [
    [sg.Menu(menu_layout)],
    [],
    [sg.Text("CAIXA ABERTO", size=(70, 1), justification='center', font=("Any", 50))],
    [sg.Text('Quantidade do Produto',size=(25,1),font=("Any", 18)),sg.InputText("1",size=(8,1),key='qtd'),
     sg.Text(" ",size=(75,1)),sg.Text(size=(23,1),key="com",justification='right',font=("Any", 18))],
    [sg.Text('Código do Produto',size=(25,1),font=("Any", 18)), sg.InputText(size=(8,1),key='lanche1'),sg.InputText(size=(76,1),key='descricao')],
    [sg.Button('OK',size=(30,1)),sg.Text("",size=(11,1)),
     sg.Button('DELETE',size=(30,1)),sg.Text("",size=(11,1)),sg.Button('PAGAR',size=(30,1)),
     sg.Text("",size=(12,1)),sg.Button('VOLTAR',size=(30,1))],
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
    elif event == "Nova Compra":
        com+=1
        window['com'].update(f'CUPOM FISCAL N°{com}')
        window["output"].update("")
        while True:
            try:
                event, values = window.read()
                if event == 'OK':
                    lanche1 = values['lanche1']
                    qtd = values["qtd"]
                    if not lanche1 :
                        sg.Text("Informe valores para continuar")
                    elif not qtd:
                        sg.Text("Informe valores para continuar")
                        continue
                    else:
                        pro=achar(lanche1)
                        if pro == lanche1:
                            qtd = int(qtd)
                            for item in dic:
                                if item["cod"] == pro:
                                    num += 1
                                    ean=item["ean"]
                                    lanche = item["lanche"]
                                    preco = item['preco'] * qtd
                                    soma2 += preco
                            dicionario = {'Comanda': com, 'Item': num,"Cod":pro,"Ean":ean, 'Lanche': lanche, 'Quantidade': qtd,
                                          'Preco': preco}
                            lista1.append(dicionario.copy())

                            for lanche in lista1:
                                pre = lanche["Preco"]
                            window['output'].print(f'       N°{"":<7}{lanche["Item"]}{"":>15}{lanche["Cod"]} - {lanche["Ean"]} - {lanche["Lanche"]:<18}{"":>20} {lanche["Quantidade"]:<18}')
                            window['output'].print(f'R$ {pre:.2f}'.rjust(140))
                            window["output"].print("      ======================================================================")
                            window['subtotal'].update(f"{soma2:.2f}")
                            window["descricao"].update(f"{lanche['Lanche']}")
                            continue
                        else:
                            continue
                elif event == 'DELETE':
                    soma2= remover(soma2)
                    window['subtotal'].update(f" {soma2:.2f}")
                    condicao=len(cancela)
                    if condicao==1:
                        window['output'].print(f'Estornado R$ {cancela[0]:.2f}'.rjust(83))
                        window["output"].print("==============================================")
                        cancela.clear()
                    continue
                elif event == 'PAGAR':
                    soma2=pagar(soma2)
                    #sg.popup_(f'Pagar R${soma2:.2f}')
                    if soma2==0:
                        lista_produto.extend(lista1)
                        lista1.clear()
                        soma2=0
                        num=0
                        window["com"].update("")
                        window["output"].update("")
                        window["subtotal"].update("")
                        break
                    else:
                        continue
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
        window["com"].update("")
        window["output"].update("")
        total()
    elif event == "Pesquisar Produto":
        window["com"].update("PESQUISAR PRODUTO")
        window["output"].print(f'{"      CÓDIGO" :<10}                      {"PRODUTO":<60}                      {"PRECO"}')
        for lanche in dic:
            window['output'].print(f'      {lanche["cod"]} - {lanche["ean"]} - {lanche["lanche"]:<18}{"":>20} ')
            window['output'].print(f'R$ {lanche["preco"]:.2f}'.rjust(140))
            window["output"].print("      ======================================================================")
            #window['output'].print(f"    {lanche['cod']:<40} {lanche['lanche']:<60} R$ {lanche['preco']:>10.2f}")
    elif event == "VOLTAR":
        window["output"].update("")
        window["com"].update("")
        continue
    elif event == "Novo Produto":
        window["com"].update("")
        window["output"].update("")
        novo_item()
    elif event == "Venda Cupom":
        window["com"].update("")
        window["output"].update("")
        venda_cupom()
    elif event == "Data":
        window["com"].update("")
        window["output"].update("")
        data=sg.popup_get_text("Data")
        window["data"].update(f'{data}')
    elif event == "Ajuda":
        sg.popup("Estamos em desenvolvimento, algumas funcionalidades podem apresentar erros,\n"
                 "Em brevo apresentaremos uma bibliotca. Aguardem!")
        continue
window.close()



#