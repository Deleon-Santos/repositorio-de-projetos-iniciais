import PySimpleGUI as sg


def converte_pdf(entrada,saida):
    nome_arquivo=entrada.docx
    saida_arquivo=saida/f"{filename}.pdf"


    





janela =[
        [sg.Text("Localizar arquivo:"),sg.Input(key="-IN-"),sg.FileBrowse(file_types=(("Texto Files",".docx",".pdf"),))],
[sg.Text("Converter arquivo:"),sg.Input(key="-OUT-"),sg.FolderBrowse()],
        [sg.Button("Sair"),sg.Button("Converter")],

]
window=sg.Window("Converson" , janela)
while True:
    evento,valor=window.read()
    if evento in (sg.WINDOW_CLOSED,"Sair"):
        break
    if evento== "Converter":
        converte_pdf(entrada=valor["-IN-"],saida=valor["-OUT-"])

        sg.popup("não habilitado")
window.close()
