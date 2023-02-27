print('\033[1;31m-=\033[m'*20)
print('Analisador de triangulo!!')
r1 = float(input('Primeiro seguimento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('\033[1;34mOs seguimento a cima podem formar um triangulo !\033[m')
else:
    print('\033[1;31mNao forma um triangulo!!\033[m')
