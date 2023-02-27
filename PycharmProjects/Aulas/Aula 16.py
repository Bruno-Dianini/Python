lanche = 'hamburguer', 'suco',  'pizza', 'batata'
for cont in range (0, len(lanche)):
    print(lanche[cont])
for comida in lanche:
    print(f'eu vou comer {comida}')
for pos , comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

print(sorted(lanche))
