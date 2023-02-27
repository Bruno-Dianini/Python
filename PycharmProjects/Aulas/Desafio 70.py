total = totalmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto:'))
    preco = float(input('Preco:R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do Programa '))
print(f'A soma dos produtos é R${total}')
print(f'{totalmil} cunta mais de R$1000')
print(f'O produto com menor preco é {barato} e o custa R${menor}')
