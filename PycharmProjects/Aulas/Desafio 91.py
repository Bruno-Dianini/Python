from random import randint
from time import sleep
from operator import itemgetter

jogador = {'Jogador1': randint(1, 6),
           'Jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),
           'Jogaddor4': randint(1, 6)}
ranking = []
print('Valores Sorteados:')
for k, v in jogador.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted((jogador.items()), key=itemgetter(1), reverse=True )
print('-=' * 30)
print('RANKING')
for i, c in enumerate(ranking):
    print(f' {i + 1}ª lugar: {c[0]} com {c[1]} ')
    sleep(1)
