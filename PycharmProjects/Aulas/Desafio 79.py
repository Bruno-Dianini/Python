numero= list()
while True:
    n= int(input('Enter a value:'))
    if n not in numero:
        numero.append(n)
        print('added value.')
    else:
        print('Repeated value will not add...')
    s= str(input('Do you want continue[Y/N]:')).upper().strip()[0]
    if s in 'Nn':
        break
print('-='*40)
numero.sort()
print(f'You have entered these value {numero}')
