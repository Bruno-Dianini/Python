#pessoas= {'nome':'Bruno','sexo':'M','idade':27}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# pessoas.keys() chaves
# pessoas.values() valores
# pessoas.items()tudo
# del pessoas['sexo']
#pessoas['nome']='leandro' subistitui
#pessoas['peso']=99 add elemento
#for k, v in pessoas.items():
# print(f'{k} = {v}')

#brasil=[]
#estado1={'uf':'Rio de janeiro','sigla': 'RJ'}
#estado2={'uf':'Sao paulo', 'sigla':'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]['uf'])

estado={}
brasil=[]
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa:'))
    estado['sigla']=str(input('Sigla do Estado:'))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O Campo {k} tem o valor {v}')# Ordernar

