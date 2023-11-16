import PySimpleGUI as sg
from docx import Document
import os
from fpdf import FPDF
def converter(entrada,saida):
    documento = Document(entrada)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for paragraph in documento.paragraphs:
        pdf.multi_cell(0, 10, paragraph.text)

    pdf_file = os.path.join(saida, os.path.splitext(os.path.basename(entrada))[0] + ".pdf")
    pdf.output(pdf_file)


sg.theme('lightBlue3')
janela = [
    [sg.Text("Localize o arquivo:",size=(15,1),font=('Time',18)), sg.InputText(key='-IN-',size=(90,1) ), sg.FileBrowse(file_types=(("Doc_Word", "*.docx"),))],
    [sg.Text("Converte o arquivo:",size=(15,1),font=('Time',18)), sg.InputText(key='-OUT-',size=(90,1) ), sg.FolderBrowse()],
    [sg.Text("",size=(40,1)),sg.Button("Converter",size=(12,1),font=('Time',12)), sg.Button("Sair",size=(12,1),font=('Time',12))],
]

window = sg.Window("Conversor de DOCX para PDF", janela,resizable=True)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Sair"):
        break
    if event == "Converter":
        entrada = values['-IN-']
        saida = values['-OUT-']
        try:
            if entrada and saida:
                try:
                    converter(entrada, saida)
                    sg.popup("Conversão concluída!", title="Sucesso")
                except Exception as e:
                    sg.popup(f"Erro na conversão: {str(e)}", title="Erro")
            else:
                sg.popup("Selecione o arquivo de entrada e o diretório de saída.", title="Erro")

        except Exception as e:
            sg.popup_error(f"Ocorreu um erro durante a conversão: {e}")

window.close()
