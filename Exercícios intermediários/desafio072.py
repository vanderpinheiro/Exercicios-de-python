while True:
    while True:
        extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze'
               ,'dezesseis','dezessete','dezoito','dezenove','vinte')

        num = int(input('Digite um número de 0 a 20:'))
        if num > 20 or num < 0:
            num = int(input('Digite um número de 0 a 20:'))
        else:
            break
    print(f'O número que você digitou foi {extenso[num]}')
    continuar = input('Quer continuar [S/N]').strip().upper()[0]
    if continuar == 'N':
        break