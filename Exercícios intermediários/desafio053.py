frase = input('Digite uma palavra para saber se ela é um Palíndromo: ').strip().upper()
palavra = frase.split()
junto = ('').join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1,-1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo')
else:
    print('Essa frase não é um palíndromo.')
