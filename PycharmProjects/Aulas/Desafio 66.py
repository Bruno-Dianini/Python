n = s = c = 0
while True:
    n = int(input('Digite um numero para parar [999]:'))
    if n == 999:
        break
    c += 1
    s += n
print(f'Voce digitou {c} e a soma foi {s}')
