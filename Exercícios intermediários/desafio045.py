import random
import time
print('-='*50)
print('{:^100}'.format('VAMOS JOGAR PEDRA, PAPEL E TESOURA'))
print('-='*50)
pc = random.randint(1,3)
if pc == 1:
   q = 'PEDRA'
elif pc == 2:
    q = 'PAPEL'
elif pc == 3:
    q = 'TESOURA'

print(''' 
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
op= int(input('Qual a sua opção? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
if op == 1:
   k = 'PEDRA'
elif op == 2:
    k = 'PAPEL'
elif op == 3:
    k = 'TESOURA'
print ('Você escolheu {} e o computador escolheu {}'.format(k,q))
if op == 1 and pc == 3 or op == 2 and pc == 1 or op == 3 and pc == 2:
    print('Você VENCEU!!!')
elif k == q:
    print('Nós EMPATAMOS!!!')
else:
    print('Você PERDEU!!!')
