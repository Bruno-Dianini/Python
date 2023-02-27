import random
print('Escolha a ordem de apresentacçao dos aulos.')
n1=input('Escreva o nome de um aluno:')
n2=input('Escreva o nome de outro aluno:')
n3= input('Escreva o nome de outro aulo:')
n4=input('Escreva o nome de outro aulo:')
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem dos alunos sera.')
print(lista)
