numeros =[[],[]]
valor=0
for c in range(0, 8):
    valor=int(input(f'Digite o {c}º valor:'))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('-='*40)
print(f'Numeros pares{numeros[0]}')
print(f'Numeros impar {numeros[1]}')
