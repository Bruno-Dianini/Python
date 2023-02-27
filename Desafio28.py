from random import randint
from time import sleep
pc= randint(0,5) # Faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar... ')
print('-=-'*20)
jg= int(input('Em qual numero pensei? '))  # jodador tenta adivinhar
print("Processando...")
sleep(3)
if jg == pc:
    print("Parabens vc acertou!")
else:
    print('Voce perdeu eu pensei {} e vc colocou {}!!'.format(pc,jg))
