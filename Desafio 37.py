num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para a conversao:
[1] Converter para Binario
[2] Converter para Octal
[3] converter para Hexadecimal''')
op = int(input('Escolha um das opções:'))
if op== 1:
    print('{} convertido para Binario é igual a {}'.format(num , bin(num)[2:]))
elif op == 2:
    print('{} convertido para Octal e igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} covertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida !!!')
