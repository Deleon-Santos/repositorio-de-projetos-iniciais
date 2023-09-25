
print('**********Sejam bem-vindoa ao Brexor Deleon da Paixao Santos********')
print()
while True:
    try:
        valor_produt o =float(input('Valor unitario do produto R$ ')  )  # entradas de valores em moeda virgente
        quantidade_produt o =int(input('Quantidade desejada? '))

        if quantidade_produt o <200: # se for menor que 200 o desconto é: 0
            total_produt o =valor_produt o *quantidade_produto
            percentua l =total_produt o * 0 /100
            total_descont o =total_produt o -percentual

        elif quantidade_produt o >199 and quantidade_produt o <1000  :# ou se for igual 200 e menor que 1000 o desconto é: 5%
            total_produto = valor_produto * quantidade_produto
            percentual = total_produto * 5 / 100
            total_desconto = total_produto - percentual

        elif quantidade_produto > 999 and quantidade_produto < 2000:  # ou se for igual a 1000 menor que 2000 o desconto é: 10%
            total_produto = valor_produto * quantidade_produto
            percentual = total_produto * 10 / 100
            total_desconto = total_produto - percentual

        else:  # senao quantidades meiores que 2000, receberão o desconto maximo de 15%dgdgdfgdgdf
            total_produto = valor_produto * quantidade_produto
            percentual = total_produto * 15 / 100
            total_desconto = total_produto - percentual
    except ValueError:
        print('digite um valor numerico')
        continue
    print('O valor total do produto sem desconto é R$ {:.2f}'.format(total_produto))
    print('O valor total do produto com desconto é R$ {:.2f}'.format(total_desconto))
    break