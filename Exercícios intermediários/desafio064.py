n = int(input('Digite um número [digite 999 para parar]: '))
t1 = 0
n1 = 0
while n != 999:
    n2 = n + n1
    n1 = n2
    n = int(input('Digite um número [digite 999 para parar]: '))
    t1 += 1

print('Você digitou {} números e soma deles é {}'.format(t1, n2))