cont = ('zero','um', 'dois', 'tres', 'quatro','cinco ', 'seis', 'sete ', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'desenove', 'vinte')
while True:
    n=int(input('Digite um numero entre 0 e 20:'))
    if 0 <= n <= 20:
        break
    print('Tente novamente ',end='')
print(f'Voce digitou o numero {cont[n]}')
