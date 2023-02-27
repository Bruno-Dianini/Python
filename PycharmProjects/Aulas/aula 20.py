def soma(a, b):
    print('-='*30)
    print(f'A= {a} e B= {b}')
    s = a + b
    print(f'A soma de A+B= {s}')


# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)


def contador(* num):
    print('-='*30)
    tam= len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 6, 2)


def dobra(lst):
    print('-='*30)
    pos=0
    while pos < len(lst):
        lst[pos] *=2
        pos+=1

valores=[6, 3, 9, 1, 0 ,2]
dobra(valores)
print(valores)


def so(*valores):
    print('-='*30)
    s=0
    for num in valores:
        s+= num
    print(f'Somando os valores {valores} temos {s}')

so(5, 2)
so(2, 9, 4)
