def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formatado=False):
    res = preco * 2
    return res if not formatado else moeda(res)


def metade(preco=0,formato=False):
    res = preco / 2
    return res if not formato else moeda(preco)

def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0,t1=10,t2=5):
    print('-'*30)
    print('Resumo do Valor.'.center(30))
    print('-'*30)
    print(f'Preco do produto:\t{moeda(preco)}')
    print(f'Metadade o produto:\t{metade(preco,True)}')
    print(f'O dobro do produto:\t{dobro(preco,True)}')
    print(f'{t1}% de aumento:\t\t{aumentar(preco,t1,True)}')
    print(f'{t2}% de diminuir:\t{diminuir(preco,t2,True)}')
    print('-'*30)