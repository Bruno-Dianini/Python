# def maior(*num):
#    print('-='*30)
#    tam=len(num)
#    print('Analizando os valores passados ...')
#    print(f'{num} foram informados {len(num)} valorens')
#    print(f'O maior valor é {max(num)}')


# maior(3,4,5,6,7,8)
# maior(5,4,5)
# maior(2,1)
# maior(0)


from time import sleep


def maior(* num):
    cont = maior = 0

    print('Analizando valores...')
    sleep(0.3)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo ')
    print(f'O maior valor {maior}')


maior(1, 3, 4, 5, 6, 8)
maior(4, 5, 6, 7)
maior(1,2,3)
maior(6)
maior()
