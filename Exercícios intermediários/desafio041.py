import datetime
ano = int(input('Digite o ano de nascimento do atleta:'))
atual = datetime.date.today().year
idade = atual - ano
if 9 >= idade:
    print('O atleta é da categoria MIRIM')
elif 9 < idade <= 14:
    print('O atleta é da categoira INFANTIL')
elif 14 < idade <= 19:
    print('O atleta é da categoai JUNIOR')
elif 19 < idade <= 25:
    print('O atleta é da categoria SÊNIOR')
else:
    print('O atleta é da categria MASTER')