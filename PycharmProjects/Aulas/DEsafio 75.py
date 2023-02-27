num =(int(input('Digite um valor:')),
      int(input('Digite outro valor:')),
      int(input('Digite outro valor:')),
      int(input('Digite outro valor')))
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 aprareceu na posição {num.index(3)+1}º')
else:
    print('Valor 3 nao encontrado')
print(f'Os valores pares digitados foram',end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
