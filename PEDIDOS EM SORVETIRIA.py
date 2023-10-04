
# QUESTÃO 2 de 4 - Conteúdo até aula 04
# Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma sorveteria. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
# A Sorveteria possui seguinte relação:
#
# ⦁	1 bola de sorvete no sabor tradicional (tr) custa 6 reais, no sabor premium (pr) 7 reais e no especial (es) 8 reais;
# ⦁	2 bolas de sorvete no sabor tradicional (tr) custam 11 reais, no sabor premium (pr) 13 reais e no especial (es) 15 reais;
# ⦁	3 bolas de sorvete no sabor tradicional (tr) custam 15 reais, no sabor premium (pr) 18 reais e no especial (es) 21 reais;
#
# Elabore um programa em Python que:
#
# ⦁	Realizar o print uma mensagem de boa s -vindas que apareça o seu nome;
# ⦁	Dev e -se entrar com o sabor (t r /p r /es) e o número de bolas de sorvete desejado ( 1 / 2 /3) [EXIGÊNCIA DE CÓDIGO 1 de 6];
# ⦁	Dev e -se executar o print da mensagem de “Quantidade de Bolas de Sorvete Inválid
# a". Se o usuário entrar com a quantidade de bolas de sorvete diferente de 1,2 e 3 repetir a partir do item B [EXIGÊNCIA DE CÓDIGO 2 de 6];
# ⦁	Dev e -se executar o print da mensagem de “Sabor de Sorvete Inválid
# o" se o usuário entrar com um sabor diferente de tr (tradicional), pr (premium) e es (especial). Printar: e repetir a partir do item B; [EXIGÊNCIA DE CÓDIGO 3 de 6];
# ⦁	Dev e -se perguntar se o cliente quer pedir mais alguma coisa. Se sim repetir a partir do item B, senão encerrar o programa printando o valor total [EXIGÊNCIA DE CÓDIGO 4 de 6];
# ⦁	Dev e -se utilizar as estruturas de whil e, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];
# ⦁	Dev e -se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
# ⦁	Dev e -se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o sabor do sorvete [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
# ⦁	Dev e -se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o número de bolas de sorvete [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];
# ⦁	Dev e -se colocar na apresentação de saída de console um pedido com duas opções sabores diferentes com quantidade de bolas diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];



#SISTEMA DE PEDIDOS EM UMA SORVEERIA
#início da funcao realce
def realce(): #composicao do cardapio
  print('--'*16,'Cardapio','-'*37)
  print('|','Nº de Bola','|','Sabor Tradicional(tr)','|','Sabor Premio(pr)', '|',' Sabor Especial(es)','|')
  print('|','    1     ', '|','        R$ 6,00      ','|','     R$ 7,00    ','|','       R$ 8,00     ','|')
  print('|','    2     ', '|','        R$ 11,00     ','|','     R$ 13,00   ','|','       R$ 15,00    ','|')
  print('|','    3     ', '|','        R$ 15,00     ','|','     R$ 18,00   ','|','       R$ 21,00    ','|')
  print('-'*79)
#final da funcao realce
#**********************************************************************************************************

#programa principal
print('-------------"Bem-vindos a Sorveteria Deleon da Paixao Santos MEI"-------------')
realce()# chamada da 'def' com o cardapio

acumulador=0 #o  acumulador retorna o valor total do pedido
print('*'*79)
while True:
  sorvete = input('Entre como o sabor desejado (tr/pr/es): ')
  sorvete = sorvete.lower()# converte as entradas maiusculas

  if sorvete != 'tr' and sorvete != 'pr' and sorvete !='es':
    print('Opcao de sorvete invalida. Tente novamente')
    print()
    continue #retorna para a pergunta se for diferente de (tr,pr,es)

  bolas=input('Entre com a quantidade de bolas de sorvete desejada (1/2/3): ')
  if bolas != '1' and bolas != '2' and bolas != '3':
    print('Opçao de bolas invalida. Tente novamente')
    print()
    continue #retorna para a pergunta se for diferente de (1,2,3)
  #-----------------------------------------------------------------------------
  if sorvete == 'tr' and bolas == '1':
    print('Voce escolheu 1 bola no sabor tradicional R$ 6,00')
    acumulador+=6
  elif sorvete == 'tr' and bolas == '2':
    print('Voce escolheu 2 bola no sabor tradicional R$ 11,00')
    acumulador+=11
  elif sorvete == 'tr' and bolas == '3':
    print('Voce escolheu 3 bola no sabor tradicional R$ 15,00')
    acumulador+=15
  #-----------------------------------------------------------------------------
  elif sorvete == 'pr' and bolas == '1':
    print('Voce escolheu 1 bola no sabor premio R$ 7,00')
    acumulador+=7
  elif sorvete == 'pr' and bolas == '2':
    print('Voce escolheu 2 bola no sabor premio R$ 13,00')
    acumulador+=13
  elif sorvete == 'pr' and bolas == '3':
    print('Voce escolheu 3 bola no sabor premio R$ 18,00')
    acumulador+=18
  #-----------------------------------------------------------------------------
  elif sorvete == 'es' and bolas == '1':
    print('Voce escolheu 1 bola no sabor especial R$ 8,00')
    acumulador+=8
  elif sorvete == 'es' and bolas == '2':
    print('Voce escolheu 2 bola no sabor especial R$ 15,00')
    acumulador+=15
  elif sorvete == 'es' and bolas == '3':
    print('Voce escolheu 3 bola no sabor especial R$ 21,00')
    acumulador=acumulador+21
  #-----------------------------------------------------------------------------
  #print()
  adicional=input('\nDigite "s" para adicionais: \n'+
                  "Outra tecla para encerrar o pedido:>>")
  adicional=adicional.lower()

  if adicional=='s':#permite que o cliente escolha mais  adicionais ao mesmo pedido
    continue
  else:
    print('*'*79)
    print('O valor total a ser pago é: R$ {:.2f}'.format(acumulador))
    print("Volte Sempre")
    break # encerra a repetição
    #final