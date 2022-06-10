palavras = ('Dormitorio','cozinha','sala','rabanete','ouvidoria','luz','penumbra'
            , 'travesseiro', 'buzina', 'mochila','carteira','garrafa','celular',
            'skate','pincel','relogio')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')