maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o {} peso:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maoir peso é {}Kg'.format(maior))
print('O menor peso e {}KG'.format(menor))
