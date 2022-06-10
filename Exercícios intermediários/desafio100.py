import random
import time
lista = []
def sorteia():
    for p in range (0,5):
        a = random.randint(1,10)
        lista.append(a)
    print(f'Os números sorteados foram:',end=' ')
    for p in lista:
        time.sleep(0.3)
        print(p,end=' ')
def somaPar():
    k=0
    for p in lista:
          if p % 2 == 0:
              k += p
    time.sleep(1)
    print(f'\nA soma dos valores pares é: {k}')


sorteia()
somaPar()