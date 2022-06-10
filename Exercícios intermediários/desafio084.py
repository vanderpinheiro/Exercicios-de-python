pessoas =[]
dados = []
pesomai = pesomen = 0
while True:
    pessoas.append(input('NOME:'))
    pessoas.append(int(input('PESO: ')))
    if len(dados) == 0:
        pesomen = pesomai = pessoas[1]
    else:
        if pessoas[1] > pesomai:
            pesomai = pessoas[1]
        if pessoas[1] < pesomen:
            pesomen = pessoas[1]

    dados.append(pessoas[:])
    resp = input('QUER CONTINUAR? [S/N] ').strip().upper()[0]
    pessoas.clear()
    if resp in 'nN':
        break
print(f' foram cadastradas {len(dados)} pessoas')
print(f'O maior peso foi de {pesomai}Kg', end=' ')
for p in dados:
    if p[1] == pesomai:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {pesomen}Kg', end=' ')
for p in dados:
    if p[1] == pesomen:
        print(p[0], end=' ')