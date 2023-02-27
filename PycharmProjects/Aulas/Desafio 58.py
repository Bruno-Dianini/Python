from random import randint
pc = randint(0,10)
print('Sou seu computador acebei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpeti?'))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais...')
        elif jogador > pc:
            print('Menos...')
print('Acertou com {} tentativas '.format(palpite))
