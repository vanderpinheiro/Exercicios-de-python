dist = float(input('Digite a distância em km da viagem que você vai fazer: '))
if dist > 200:
    prec = 0.45*dist
    print('O preço da sua passagem é R${:.2f}'.format(prec))
else:
    prec = 0.5*dist
    print('O preço da sua passagem é R${:.2f}'.format(prec))
