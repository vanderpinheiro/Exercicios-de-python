num = int(input('Digite um número para saber o fatorial dele: '))
d = num
g = 1
while d > 0:
    print('{}'.format(d), end='')
    g *= d
    d -= 1
print('O fatorial desse número é: {} '.format(g))