operadores = ["+", "-", "*","/"]
numeros=["1","2","3","4","5","6","7","8","9"]
manter = ""
operacao = ""
numeros = [str(i) for i in range(0, 10)]#uma laço para gerar "0 a 9 convertidos em str

while True:
    if event=="Clear":
        window["-OUT-"].update("")   
   
    elif event in numeros:
        if not operacao:
            if len(manter) < 17:
                manter += event
                window["out"].update(manter)
                numero=event
        else:
            manter+=event
            numero_2=event
            window["out"].update(manter)
    elif event in operadores:
        operacao=event
        if event not in manter:
            manter += event
        else:
            manter = manter[:-1] + event  #
        window["out"].update(manter)
    elif event == "=":
        if operacao:
            
            if operacao == "+":
                resp =str(float (numero)+ float(numero_2))
            elif operacao == "-":
                resp =str(float (numero)- float(numero_2))
            elif operacao == "*":
                resp =str(float (numero)* float(numero_2))
            elif operacao == "/":
                if numero_2 != 0:
                    resp =str(float (numero)/ float(numero_2))
                else:
                    resp = "Erro"
            manter = (f"{resp}".replace(".0",""))
            window["out"].update(manter)
            
            operacao = ""
            numero=(manter)
            numero_2=''
    elif event=="<":
        if len(manter):
            manter=manter[:-1]
            window["out"].update(manter)
    elif event == "c":
        manter = ""
        operacao = ""
        window["out"].update("0")
    elif event == "+/-":
        manter=str(float(manter) * -1)
        window["out"].update(manter)
    elif event==".":
        if "." not in manter:
            manter += "."
            window["out"].update(manter)
    elif event == "%":
        if operacao:
            
            porcentagem = float(numero) * (float(manter) / 100)  # Convertendo para porcentagem
            numero_2 = porcentagem

            if operacao == "+":
                resp = str(float(numero) + numero_2)
            elif operacao == "-":
                resp = str(float(numero) - numero_2)
            elif operacao == "*":
                resp = str(float(numero) * numero_2)
            elif operacao == "/":
                if numero_2 != 0:
                    resp =str(float (numero)+ float(numero_2))
                else:
                    manter = "Erro"
            #manter = (f"{resp}".replace(".0",""))
            window["out"].update(resp)
            numero=manter 
            operacao = ""
            numero_2=''
    print(manter)

        