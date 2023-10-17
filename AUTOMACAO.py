# importe a biblioteca para automação
#auto-py-to-exe
import pyautogui as pa
#liste todos os links da automação
lista=["https://colab.research.google.com/drive/1gss2ecOzRXtUdBUVhQjFzPjx_ZA-P6tH",
       "https://www.linkedin.com/feed/",
       "https://www.ev.org.br/cursos"]
#emita alertas do inicio do sistema
pa.alert("Abrindo as Ferramentas")
pa.PAUSE=0.7
pa.press("winleft")
pa.write("chrome")
pa.press("enter")
#inicio da apesquisa no navegador dependo da velocidade da conexao
pa.sleep(1.5)
#para todos os itens da lista faça
for i in lista:
    pa.write(i)
    pa.press("enter")
    pa.hotkey("ctrl", "t")
#
