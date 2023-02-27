brasileirao = ('Atletico-MG','Flamengo','Palmeiras', 'Fortaleza', 'Corintians', 'Bragantino', 'Fluminence',
               'America-MG','Atletico-GO','Santos','Ceara','Internacional','São Paulo', 'Atleto-PR','Cuiaba',
               'Juventude', 'Gremio','Baiha', 'Sport', 'Chapeconse')
print('=-'*30)
print(f'Lista do Brasileirão : {brasileirao}')
print('-='*30)
print(f'Os cinco primeiros times são{brasileirao[0:5]}')
print('-='*30)
print(f'Os ultimos quatro colocados são {brasileirao[-4:]}')
print('-='*30)
print(f'Ordem Alfabetica:{sorted(brasileirao)}')
print('=-'*30)
print(f'O Chapecoense esta na {brasileirao.index("Chapeconse")+1} posição.')
print('=-'*30)
