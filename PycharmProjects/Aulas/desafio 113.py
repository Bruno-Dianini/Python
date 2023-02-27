def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('\033[31mErro!Digite um valor valido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mEntradas de dados entenrrompidas pelo usuario.\033[m')
        else:
            return n


num=leiaint('Digite um numero inteiro:')
print(f'O valor digita foi {num}')
