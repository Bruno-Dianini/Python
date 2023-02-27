frase= str(input('Digite uma frase.')).upper().strip()
print('A lentra A aparece {} na frase:'.format(frase.count('A')))
print('A primeira letra A aparece na posicao: {}'.format(frase.find('A')+1))
print(' A ultima letra A aparece na posiçao: {}'.format(frase.rfind('A')+1))
