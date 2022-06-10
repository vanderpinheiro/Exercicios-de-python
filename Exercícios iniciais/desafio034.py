sal = float(input('Digite o valor do seu salário:'))
if sal > 1250:
    salaum = sal*1.1
    print('O seu novo salário com aumento de 10% é de R${:.2f}'.format(salaum))
else:
    salaum = sal*1.15
    print('O seu novo salário com aumento de 15% é de R${:.2f}'.format(salaum))