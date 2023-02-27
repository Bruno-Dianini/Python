from time import sleep
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('\033[32mPrimeiro termo: '))
razao = int(input('\033[35mRazão:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[34m{} -'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('\033[34mQuantos termos vc quer mostrar a mais?'))
    sleep(1)
print('\033[33mProgressao finalizada com {} termos'.format(total))
