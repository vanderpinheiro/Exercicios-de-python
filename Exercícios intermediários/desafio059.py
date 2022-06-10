a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = 0
d = 0
while d != 5:
    d = int(input(''' Digite uma opção desejada
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA 
    
    '''))
    if d == 1:
        c = a+b
        print('O valor da soma é {}'.format(c))
    elif d == 2:
        c = a*b
        print('O valor da multiplicação é {}'.format(c))
    elif d == 3:
        c = a
        if b> a:
            c = b
        print('O maior número digitado é o {}'.format(c))
    elif d == 4:
        print('Digite novamente os número..')
        print('')
        a = int(input('Digite um número: '))
        b = int(input('Digite outro número: '))
    elif d == 5:
        print('Ok...')
        print('Saindo do programa.')
