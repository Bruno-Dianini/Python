listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Dgite um valor para a posicap {c}:')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('-' * 30)
print(f'Voce digitou os valores{listanum}')
print(f'O maior valor digitado foi {maior} nas posiçao ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posiçao ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end=' ')
print()
