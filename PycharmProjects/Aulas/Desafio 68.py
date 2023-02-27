from random import randint
v = 0
print('-='*30)
print('\033[34m Vamos jogar par ou impar!!\033[m')
print('-='*30)
while True:
    j =int(input('Digite um valor:'))
    pc = randint(0, 10)
    total = j + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar?[P/I]')).strip().upper()[0]
    print(f'Voce jogou {j} e o computador {pc}.O total foi {total} ', end='')
    print('Deu par'if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu !!')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
            v +=1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente ...')
print(f'Voce venceu tantas vezes {v}.')
print('Game over!!!')