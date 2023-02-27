aluno={}
aluno['nome']=str(input('Nome:'))
aluno['media']=float(input(f'Media de {aluno["nome"]} :'))
if aluno['media'] >= 7:
    aluno['Situacao']='Aprovado'
elif aluno['media'] <= 5:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao']= 'Recuperaçao'
print('-='*30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
