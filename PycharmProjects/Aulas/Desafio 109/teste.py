import moeda

p=float(input('Digete um preço:R$'))
print(f'O Dobro de {moeda.moeda(p)} e {moeda.dobro(p,True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True )}')
print(f'Aumentando 10% é {moeda.aumentar(p,10,True)}')
print(f'Diminuindo 1% sao {p -moeda.diminuir(p,1,True)} de desconto')
