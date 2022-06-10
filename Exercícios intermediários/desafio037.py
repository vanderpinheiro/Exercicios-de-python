num = int(input('Digite um número inteiro:'))
print(''' Escolha uma das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção? '))
if op == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} convertido para octal é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Digita a porra do número certo caralho')