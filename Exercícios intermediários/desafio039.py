import datetime
sex = input('Você é do sexo MASCULINO? S/N   ').upper().strip()
if sex == 'N':
    print('Ok, tenha um bom dia!')
else:
    ano = int(input('Em que ano você nasceu?'))
    year = datetime.date.today().year
    idade = year - ano
    print('Você tem {} anos.'.format(idade))
    if idade > 18:
        print('Você é maior de idade e já passou da fase de se alistar nas Forças Armadas.')
    elif idade == 18:
        print('Você está na idade de se alistar. Procure um posto de alistamento das Forças Armadas')
    else:
        falta = 18 - idade
        print('Você ainda é menor de idade. Daqui a {} anos você deve procurar um posto de alistamento militar.'.format(falta))
