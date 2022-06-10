frase = input('Digite uma frase: ').strip()
print('Esta frase tem {} letras A'.format(frase.lower().count('a')))
print('O primeiro A aparece na posição {}'.format(frase.lower().find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.lower().rfind('a')+1))

