import random
n = (random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999))
print(f'Os números gerados na tupla foram: ',end='')
for t in n:
    print(t, end=' ')

print(f'\nA tupla em ordem é {sorted(n)}')
#print(f'O menor número é o {sorted(n)[0]}')
#print(f'O maior número é o {sorted(n)[4]}')
print(f'O menor número é o {max(n)}')
print(f'O maior número é o {min(n)}')