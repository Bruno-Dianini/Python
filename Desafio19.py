import random
n1=input('Escreva o nome de um aluno:')
n2=input('Escreva o nome de outro aluno:')
n3=input('Escreva o nome de outro aluno:')
n4=input('Escreva o nome de outro aulo :')
lista= [n1 ,n2, n3, n4]
escolhido= random.choice(lista)
print('O aluno escolhi foi {}.'.format(escolhido))
