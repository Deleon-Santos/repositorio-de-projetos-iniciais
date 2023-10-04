#QUESTAO "1" DO TRABALHO DE LOGICA E PROGRAMAÇÃO
#Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade as informações abaixo:

#⦁	Se quantidade for menor que 200 o desconto será de 0%;
#⦁	Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
#⦁	Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
#⦁	Se quantidade for igual ou maior que 2000 o desconto será de 15%;

#Elabore um programa em Python que:
#⦁	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
#⦁	Deve-se entrar com o valor unitário e quantidade do produto [EXIGÊNCIA DE CÓDIGO 1 de 4];
#⦁	Deve-se retornar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 2 de 4];
#⦁	Deve-se utilizar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 3 de 4];
#⦁	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 4 de 4];


print('**********Sejam bem-vindoa ao Brexor Deleon da Paixao Santos********')
print()
while True:
    try: #com laço while para tratar erros
        valor_produto = float(input('Valor unitario do produto R$ '))  # entradas de valores em moeda virgente
        if valor_produto >0:
            while True:
                quantidade_produto  = int(input('Quantidade desejada? '))

                if quantidade_produto >0 and quantidade_produto < 200: # se for menor que 200 o desconto é "0"
                    total_produto = valor_produto * quantidade_produto
                    percentual = 0*total_produto/100 #formula para calcular o percentual
                    total_desconto = total_produto - percentual
                    print(f"O valor total do produto sem desconto é R$ {total_produto:.2f}")
                    print(f"O valor total do produto com desconto é R$ {total_desconto:.2f}")
                    break#fim do laço quantidade

                elif quantidade_produto >199 and quantidade_produto <1000: # ou se for igual 200 e menor que 1000 o desconto é: 5%
                    total_produto = valor_produto * quantidade_produto
                    percentual = 5*total_produto/100
                    total_desconto = total_produto - percentual
                    print(f"O valor total do produto sem desconto é R$ {total_produto:.2f}")
                    print(f"O valor total do produto com desconto é R$ {total_desconto:.2f}")
                    break#fim do laço quantidade

                elif quantidade_produto > 999 and quantidade_produto < 2000:  # ou se for igual a 1000 menor que 2000 o desconto é: 10%
                    total_produto = valor_produto * quantidade_produto
                    percentual = 10 * total_produto / 100
                    total_desconto = total_produto - percentual
                    print(f"O valor total do produto sem desconto é R$ {total_produto:.2f}")
                    print(f"O valor total do produto com desconto é R$ {total_desconto:.2f}")
                    break#fim do laço quantidade
                elif quantidade_produto >1999:  # senao quantidades meiores que 2000, receberão o desconto maximo de 15%dgdgdfgdgdf
                    total_produto = valor_produto * quantidade_produto
                    percentual = 15 * total_produto / 100
                    total_desconto = total_produto - percentual
                    print(f"O valor total do produto sem desconto é R$ {total_produto:.2f}")
                    print(f"O valor total do produto com desconto é R$ {total_desconto:.2f}")
                    break#fim do laço quantidade
                else:
                    print("A quantidade não pode ser 'zero'")
                    continue#continua pedindo o valor
        else:
            print("O valor não pode ser 'zero'")
            continue#continua pedindo o valor
    except ValueError:#trata erro de valor não numerico
        print('Digite um valor numerico')
        continue
    break# encerra o sistema

    #fim
