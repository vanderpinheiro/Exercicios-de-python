import datetime
atual = (datetime.date.today().year)
totmaior = 0
totmenor = 0
for c in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior+1
    else:
        totmenor = totmenor+1
print('Existem {} pessoas maiores de idade'.format(totmaior))
print('Existem {} pessoas menores de idade'.format(totmenor))