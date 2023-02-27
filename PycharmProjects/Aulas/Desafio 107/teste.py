import desafio107

p=float(input('Digete um preço:R$'))
print(f'O Dobro de R${p} e R${desafio107.dobro(p)}')
print(f'A metade de R${p} é R${desafio107.metade(p)}')
print(f'Aumentando 10% é {desafio107.aumentar(p,10)}')
print(f'Diminuindo 1% sao R${p -desafio107.diminuir(p,1)} de desconto')
