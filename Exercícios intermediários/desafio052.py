num = int(input('Digite um número:'))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        tot = tot +1

if tot == 2:
    print('\nEsse número é PRIMO')
else:
    print('\nEsse número não é PRIMO')
