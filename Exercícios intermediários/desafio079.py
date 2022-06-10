num = []

while True:
    c = (int(input('Digite um valor: ')))
    if c not in num:
        num.append(c)
    else:
        print('Esse número já foi adicionado. Tente novamente')
    resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp in 'N':
        break

print(f'Os valores que você digitou foram {num}')
print(f'Os valores em ordem crescente foram: {sorted(num)}')