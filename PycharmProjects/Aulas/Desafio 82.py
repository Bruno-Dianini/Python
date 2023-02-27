n = []
par = []
impar = []
while True:
    n.append(int(input('Digite um valor:')))
    s = str(input('Quer continuar [S/N]:')).strip()[0]
    if s in 'Nn':
        break
for i, v in enumerate(n):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-='*30)
print(f'Todos os valores {n} ')
print(f'numeros par {par}')
print(f'numerods impar {impar}')
