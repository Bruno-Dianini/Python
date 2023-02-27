jogador={}
partidas=[]
jogador['nome']=str(input('Nome do jogador:'))
tot=int(input(f'Quatas partidas jogou {jogador["nome"]} ?:'))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gol na partida {c+1}?:')))
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)
print('-='*30)
print(jogador)
print('=-'*30)
for k, i in jogador.items():
    print(f'O campo {k} tem o valor {i}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i,v in enumerate(jogador['gols']):
    print(f'=> Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')
