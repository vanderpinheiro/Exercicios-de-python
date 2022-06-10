matriz=[[0,0,0],[0,0,0],[0,0,0]]
par = d = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)
for l in range(0,3):
    for c in range (0,3):
        if matriz[l][c]%2 == 0:
            par += matriz[l][c]
for l in range(0,3):
    d += matriz[l][2]
for c in range (0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma dos valores pares da matriz é {par}')
print(f'A soma dos valores da terceira coluna é {d}')
print(f'O maior valor da segunda linha é {maior}')

