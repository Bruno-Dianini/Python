num = int(input('Digite um numero:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[35m O numero {} foi divisivel {} vezes\033[m'.format(num, tot))
if tot == 2:
    print('Por isso ele é primo.')
else:
    print('Não é primo')
