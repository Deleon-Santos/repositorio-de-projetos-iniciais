#TABOADA DE 1 AO 10 COM ESTRUTURAS WHILE E FOR CONTENDO AS 4 OPERAÇÕES MATEMATICAS

#função de '*'
def multiplicacao():
  print('Multiplicacao de 1 a 10')
  n=0 #"N" representa o numero
  while n<10:#enquanto "n" for menor <= 10
    n+=1 # "n" recebe um iterado
    c=0# "C" representa o multipicador
    print()
    print(f'taboada {n}')
    print()
    print(f'{n}*{c}={n*c}')
    for c in range (10):#para "c" ate  10
      c+=1
      print(f'{n}*{c}={n*c}')

#função de '/'
def divisao():
  print('Divisao de 1 a 10')
  n=0
  while n<10:
    n+=1
    c=1
    print()
    print(f'taboada {n}')
    print()
    print(f'{n}/{c}={n/c:.1f}')
    for c in range (10):
      c+=1
      print(f'{n}/{c}={n/c:.1f}')

#função de '-'
def subitracao():
  print('Subitracao de 1 a 10')
  n=0
  while n<10:
    n+=1
    c=0
    print()
    print(f'taboada {n}')
    print()
    print(f'{n}-{c}={n-c}')
    for c in range (10):
      c+=1
      print(f'{n}-{c}={n-c}')

#função de '+'
def adicao():
  print('Adicao de 1 a 10')
  n=0
  while n<10:
    n+=1
    c=0
    print()
    print(f'taboada {n}')
    print()
    print(f'{n}+{c}={n+c}')
    for c in range (10):
      c+=1
      print(f'{n}+{c}={n+c}')

#pograma principal e chamada das fincoes
adi=adicao()
print(adi)
sub=subitracao()
print(sub)
mult=multiplicacao()
print(mult)
div=divisao()
print(div)