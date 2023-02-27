al=float(input('Percorrido:'))
dia=int(input('Dias de aluguel:'))
km=al*0.15 + dia*60
print('O carro foi alugado e percoreu {}KM e foi usado por {} dias o valor do alugué é R${:.2f} '.format(al,dia,km))
