def ficha(jogar= '<desconhecido>',gol=0):
    print(f'O {jogar} fez {gol} glos no campeonato')


n=str(input('Digite o nome do jogador:'))
g=str(input('Quantos gols ele fez:'))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
