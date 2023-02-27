from time import sleep
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro:'))
opçao = 0
while opçao != 5:
    print('''
    >>>>Qual é sua opção?
    [1] somar
    [2] multiplicar
    [3] maior
    [4]novos numeros 
    [5]sair do programa''')
    opçao= int(input('Qual sua opção?'))
    if opçao == 1:
        soma = n1 +n2
        print('A soma de {} e {} é {}'.format(n1, n2, soma))
    elif opçao == 2:
        multi = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1, n2 , multi))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior é {}'.format(n1,n2, maior))
    elif opçao == 4:
        print('Informe os numerios novamente.')
        n1 = int(input('Digite um valor:'))
        n2 = int(input('Outro valor:'))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida tente novamente!!')
    print('=-='* 10)
    sleep(2)
print('Fim do programa!Volte sempre!')
