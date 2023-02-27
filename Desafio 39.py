from datetime import date
atual = date.today().year
nasc = int(input('Ano do nascimento :'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc , idade, atual))
if idade == 18:
    print(' Voce tem que se alistar imediatamente!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera  {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(' Voce ja deveria ter se alista a {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))
