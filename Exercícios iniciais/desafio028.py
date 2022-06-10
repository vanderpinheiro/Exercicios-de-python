import random
import time
m = int(random.randint(0,5))
k = int(input("Pensei em um número. Digite um número de 0 a 5 para ver se você acerta em qual eu pensei: "))
print("PROCESSANDO....")
time.sleep(1)

if k == m:
    print('Parabéns, você acertou o número. VOCÊ É FERA!')
else:
    print('Errou. Tomou no cu')