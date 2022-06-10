lista = [[],[]]
for p in range (0,7):
    c=(int(input(f'Digite o {p+1}º número: ')))
    if c % 2 == 0:
        lista[0].append(c)
    else:
        lista[1].append(c)
sorted(lista[0])
sorted(lista[1])
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')