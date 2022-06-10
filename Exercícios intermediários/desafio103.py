def ficha(n=0,g=0):
    if n in '':
        n='<desconhecido>'
    if g in '':
        g = 0
    print(f'O jogador {n} fez {g} gols no campeonato.')


nome=input('Digite o nome do jogador: ').strip()
gols = input('Digite a quantidade do gols do jogador:')

ficha(nome,gols)