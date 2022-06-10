valor = float(input('Digite o preço do produto: R$'))
forpag = input('''Digite a forma de pagamento:
                [1] à vista em dinheiro ou cheque
                [2] à vista no cartão 
                [3] 2x no cartão
                [4] 3x ou mais no cartão
                
                ''')
if forpag == '1':
    precf = valor * 0.9
    print('O valor do produto é R${}, mas pagando à vista você pagará'
          ' com 10% de desconto o valor de R${}'.format(valor,precf))
elif forpag == '2':
    precf = valor * 0.95
    print('O valor do produto é R${}, mas pagando à vista no cartão você pagará'
          ' com 5% de desconto o valor de R${}'.format(valor, precf))
elif forpag == '3':
    print('O valor do produto é R${}, pagando em 2x a parcela será de R${} por mês'.format(valor,valor/2))
elif forpag == '4':
    valor1= valor *1.2
    prest = int(input('Quantas prestações? '))
    print('O valor do produto é R${}, pagando em {}x terá um aumento de 20% no preço do produto, '
          'passando a ser R${} e a parcela será de R${} por mês'.format(valor, prest, valor1, valor1 / prest))
else:
    print('Opção inválida!!!')

