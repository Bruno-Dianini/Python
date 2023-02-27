c = float(input('Valor da casa :R$'))
s = float(input('Slario do comprador :R$'))
anos = int(input('Quantos anos de finaciamento ?'))
prestacao = c/(anos*12)
minimo = s*30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(c, anos), end='')
print('A prestacao sera de RS{}'.format(prestacao))
if prestacao <= minimo:
    print('O emprestimo pode ser concedido ')
else:
    print('\033[1;32m O emprestimo nao pode ser concedido \033[m')
