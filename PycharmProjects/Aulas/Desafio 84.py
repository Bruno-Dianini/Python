temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar[S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Total de pessoas cadastradas {len(princ)} ')
print(f'O maior peso é {mai}Kg ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso é {men}Kg ', end='')
for b in princ:
    if b[1] == men:
        print(f'[{b[0]}]', end='')
print()
