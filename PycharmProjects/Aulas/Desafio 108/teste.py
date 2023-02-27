import moeda

p=float(input('Digete um preço:R$'))
print(f'O Dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 10% é {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo 1% sao {moeda.moeda(p -moeda.diminuir(p,1))} de desconto')
