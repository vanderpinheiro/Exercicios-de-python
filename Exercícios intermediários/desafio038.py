m = int(input('Digite um número:'))
n = int(input('Digite outro número:'))
if m > n:
    print('O número {} é o maior e o número {} é o menor'.format(m,n))
elif n > m:
    print('O número {} é o maior e o número {} é o menor'.format(n, m))
else:
    print('Os números são iguais.')