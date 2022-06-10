import random
import time
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista=[]
print(f'SORTEANDO {jogos} JOGOS')
print('-='*20)
for c in range (0,jogos):
    for l in range (0,6):
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
        lista.sort()
    print(f'jogo {c+1} = {lista}')
    time.sleep(1)
    lista.clear()
print('-=' * 20)
print('{:^35}'.format('<BOA SORTE>'))