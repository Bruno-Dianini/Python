nome=str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome ...')
print('Seu nome em maisculo é {}'.format(nome.upper()))
print('Seu nome em letra minuscula {}'.format(nome.lower()))
print('Letras no seu nome {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa= nome.split()
print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
