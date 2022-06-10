homemvelho = ''
homemidademaior = 0
idades = 0
midade = 0
mulheresnovas = 0
for c in range(1,5):
    nome = input('Digite o nome da {}ª pessoa: '.format(c)).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = input('Digite o sexo da {}ª pessoa [M/F]: '.format(c)).strip().upper()
    if idade > homemidademaior and sexo in 'Mm':
        homemidademaior = idade
        homemvelho = nome
    idades =  idades + idade
    midade = idades/c
    if sexo in 'Ff' and idade < 20:
        mulheresnovas = mulheresnovas + 1
print('O nome do homem mais velho é {}.'.format(homemvelho))
print('A média de idade do grupo é {:.2f} anos'.format(midade))
print('Existem {} mulheres que tem menos de 20 anos'.format(mulheresnovas))