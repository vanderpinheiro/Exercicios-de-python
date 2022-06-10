print('-='*20)
print('\033[0:31:40mFAÇA AQUI A  CONSULTA PARA EMPRÉSTIMO!!\033[m')
print('-='*20)
valorcasa = float(input('Qual é o valor da casa que você quer comprar? R$'))
sal: float = float(input('Qual é o seu salário? R$'))
ano = int(input('Em quantos anos pretende pagar a casa?'))
qprest= ano*12
prest = valorcasa/qprest

print('A casa vale R${}, seu salário é de R${}, a prestação ficará em R${:.2f} mensais.'.format(valorcasa,sal,prest))

if prest > (0.3*sal):
    print(''' EMPRÉSTIMO NEGADO!!!
        Você não tem condições de fazer este tipo de empréstimo. 
        Compre uma casa mais barata ou aumente o número de parcelas''')
else:
    print('''EMPRÉSTIMO APROVADO. 
          VEM SER FELIZ FILHO DA PUTINHA''')
    print('Sua parcela será de {:.2f}'.format(prest))