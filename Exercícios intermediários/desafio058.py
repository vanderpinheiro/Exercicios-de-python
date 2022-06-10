import random
import time
choice = random.randint(1,10)
c = 1
print('-='*35)
print('\033[:33:40mPensei em um número. Vamos ver se você é bom mesmo.... Tente acertar\033[m')
print('-='*35)
chute = int(input())
while chute != choice:
    print('hmmm. Deixa eu verificar......')
    time.sleep(1)
    chute = int(input('Errroo. Tente novamente: '))
    print('')
    c = c+1

print('hmmm. Deixa eu verificar......')
print('')
time.sleep(1)
print('Você acertou. Parabéns!!!!')


print('Você precisou de {} tentativas para acertar o meu número.'.format(c))