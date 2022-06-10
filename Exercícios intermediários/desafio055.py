pesomaior = 0
pesomenor = 0
cas = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa em KG: '.format(c)))
    if c==1:
        pesomaior = peso
        pesomenor = peso
    else:
        if pesomaior < peso:
            pesomaior = peso
        elif pesomenor > peso:
            pesomenor = peso


print('A pessoa mais pesada pesa {} e a pessoa menos pesada pesa {}kg'.format(pesomaior, pesomenor))