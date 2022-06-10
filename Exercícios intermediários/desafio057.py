sexo = input('Digite o sexo da pessoa selecionada [M/F]: ').upper().strip()
while sexo != 'M' and sexo != 'F' :
    print('Você digitou um sexo inválido. Tente novamente:')
    sexo = input('Escolha um sexo [M/F]: ').upper().strip()
print('Você acertou!! Obrigado')

