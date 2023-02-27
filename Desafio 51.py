#Progressao arritmetica DE uma PA
pri = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = pri + (10-1) * razao
for c in range(pri, decimo+razao, razao):
    print('{}'.format(c), end=' - ')
print('Acabou')
