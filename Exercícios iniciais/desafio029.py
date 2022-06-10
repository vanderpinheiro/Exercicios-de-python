vel = int(input('Digite a velocidade em que o carro estava:'))
if  vel > 80.0:
    multa = (vel - 80)*7
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Tudo bem, você não foi multado.')