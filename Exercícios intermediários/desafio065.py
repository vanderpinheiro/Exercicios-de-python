resp = 'S'
soma = 0
média = 0
cont= 0
n1 = n2 = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    soma = soma + num
    cont += 1
    if cont == 1:
       n1 = n2 = num
    else:
        if num > n1:
            n1 = num
        if num < n2:
            n2 = num
    resp = str(input('Quer continuar [S/N]')).strip().upper()[0]

média = soma/cont

print('A soma dos números digitados é {} e a média {}'.format(soma, média))
print('O maior número digitado é {} e o menor é {}'.format(n1, n2))
print('FIM')