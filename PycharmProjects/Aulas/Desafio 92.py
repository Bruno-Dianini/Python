from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho[0 não tem]:'))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao:'))
    dados['salario'] = float(input('Salario:'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 35) - datetime.now().year
print('-=' * 30)
for v, i in dados.items():
    print(f'- {v} tem o valor {i}')
print('-=' * 30)
