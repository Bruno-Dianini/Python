n=[]
cont = 0
while True:
    n.append(int(input('Digite um valor:')))
    resp=str(input('Quer continuar [S/N]:')).strip()[0]
    if resp in 'Nn':
        break
print('-='*40)
n.sort(reverse=True)
print(f'Voce Digitou {len(n)} valores')
print(f'Na ordem descrescente {n}')
if 5 in n:
    print('O valor 5 faz parte da lista.')
else:
    print('o valor 5 nao faz parte da lista ')
