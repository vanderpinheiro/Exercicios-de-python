pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
res = 0
c = 1
d = 0
ufa = 10
total = 0
print('{} → '.format(pt), end='')
while ufa != 0:
    total = total + ufa
    while c < total:
        res = pt + rz
        pt = res
        c = c + 1
        print('{} → '.format(res), end='')

    print(' PAUSA')
    ufa = int(input('Você quer saber quantos termos a mais?'))
