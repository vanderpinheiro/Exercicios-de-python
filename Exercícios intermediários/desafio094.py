pessoas = {}
geral = []
soma = c = 0
while True:
    pessoas['nome'] =input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo [M/F] ').strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    geral.append(pessoas.copy())
    resp = input('Quer continuar [S/N] ').strip().upper()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'- Foram cadastradas {len(geral)} pessoas')
for p in range (0,len(geral)):
    soma += geral[p]['idade']

media = (soma/len(geral))
print(f'- A média de idade é de {media:.2f}')

print('- As mulheres cadastradas foram:', end=' ')
for p in range (0,len(geral)):
    if geral[p]['sexo'] == 'F' :
        print(geral[p]['nome'], end=' ')
print()

print('- Lista de pessoas que estão acima da média:')
for p in range (0,len(geral)):
    if geral[p]['idade'] >= media:
        print(geral[p])

print(geral)
print('<<ENCERRADO>>')