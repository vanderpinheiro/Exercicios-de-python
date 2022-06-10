def leiaint(num):
    ok = False
    valor = 0
    while True:
        n=input(num)
        if n.isnumeric():
            valor=int(n)
            ok = True
        else:
            print('\033[31mERRO! você não digitou um número.\033[m')
        if ok:
            break
    return valor

n = leiaint('digite um número: ')
print(f'Você acabou de digitar o número {n}')