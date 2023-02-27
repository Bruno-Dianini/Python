print('{:=^40}'.format('Lojas Dianinis'))
preco = float(input('Preço da compra: R$'))
print('''Forma de pagamento
[1] a vista dinheiro / cheque
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
op = int(input('Qual é a opção?'))
if op == 1:
    total = preco - (preco * 10 / 100)
elif op == 2:
    total = preco - (preco * 5 /100)
elif op == 3:
    total = preco
    parcela = total/ 2
    print('Sua compra sera parcelada em 2x de R${:.2f} Sem Juros'.format(parcela))
elif op ==4:
    total = preco + (preco * 20 / 100)
    totalpa = int(input('Quantas parcelas ?'))
    parcela = total / totalpa
    print('Sua compra sera parcelada em {}x de R${:.2f}.Com Juros'.format(totalpa, parcela))
else:
    total = preco
    print("opçao invalida de pagamento. Tente novamente! ")
print('Sua compra de {:.2f} vai custar {:.2f} no final'. format(preco, total))
