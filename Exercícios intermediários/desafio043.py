alt = float(input('Digite a sua altura em metros:'))
peso = float(input('Digite o seu peso em kg:'))
imc = peso/alt**2
print('Seuy IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5<= imc <25:
    print('Peso ideial')
elif 25<= imc < 30:
    print('Sobrepeso')
elif 30 <= imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

