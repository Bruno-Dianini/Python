nome = str(input('Qual é seu nome ?'))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Bruno' or nome == 'Maria ' or nome == 'Jõao':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem comum')
print('É um prazer em te conhecer {} !!!'.format(nome))
