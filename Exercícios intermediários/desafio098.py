import time

def contador(a,b,c):
    d = 0
    if a < b:
        print('-=' * 40)

        print(f'Contando de {a} até {b} de {c} em {c}:')
        while d <= b:
            print(a, end=' ')
            d = a + c
            a = d
        print()

    elif b < a:
        print('-=' * 40)
        print(f'Contando de {b} até {a} de {c} em {c}')
        d = a
        while d >= b:
            print(a, end=' ')
            d = a - c
            a = d
        print()

    elif a == 0 and b == 0 and c == 0:
        print('-=' * 40)
        print('Agora é sua vez de personalizar sua contagem!')
        a = int(input('Início: '))
        b: int = int(input('Fim: '))
        c = int(input('Passo: '))
        print('-='*40)
        if c == 0:
            c = 1
        if c < 0:
            c = c*(-1)

        if a < b:
            print(f'Contando de {a} até {b} de {c} em {c}')

            while d <= b:
                print(a, end=' ')
                d = a + c
                a = d
            print()
        elif a > b:
            print(f'Contando de {b} até {a} de {c} em {c}')
            d = a
            while d >= b:
                print(a, end=' ')
                d = a - c
                a = d
            print()

#cod principal
contador(1,10,1)
contador(10,0,2)
contador(0,0,0)