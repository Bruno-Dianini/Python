# teste = list()
# teste.append('Bruno')
# teste.append(27)
# galera =list()
# galera.append(teste[:])
# teste[0]= 'Daneil'
# teste[1]= 47
# galera.append(teste[:])
# print(galera)

#galera = [['joao', 19],['marta', 22],['felipe', 45],['breno', 13]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos')

galera=[]
dado=[]
totmaior= totmenor=0
for c in range(0,3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'temos {totmaior} maiores de idade e menores de idade {totmenor}')
