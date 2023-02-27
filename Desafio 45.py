from random import randint
print('{:=^40}'.format('É hora do DUELO!!'))
intens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jg = int(input('Qual é sua jogada:'))
print('=-'*20)
print("Computador jogou {}".format(intens[pc]))
print('Jogador jogou {}'.format(intens[jg]))
print('=-'*20)
if pc == 0: # pc jogou pedra
    if jg == 0:
        print('Empate')
    elif jg == 1:
        print('Jogador venceu!')
    elif jg == 2:
        print('Computador venceu!')
    else:
        print('Opção invalida !!')
elif pc == 1: # pc jogou papel
    if jg == 0:
        print('Computador venceu!!')
    elif jg == 1:
        print('Empate!!')
    elif jg == 2:
        print('Jodagor venceu!!')
    else:
        print('Opção Invalida!!')
elif pc == 2:
    if jg == 0:
        print('O jogador venceu!')
    elif jg == 1:
        print('O computador venceu!!')
    elif jg == 2:
        print('Empate!!')
    else:
        print('Opção Invalida!!')
