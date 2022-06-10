time = []
dados ={}
lista=[]
c = 0
while True:
    dados.clear()
    dados['jogador'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
    lista.clear()
    for p in range (0,partidas):
        lista.append( int(input(f'Quantos gols na partida {p+1}?')))
    dados['gols'] = lista[:]
    dados['total'] = sum(lista)
    time.append(dados.copy())
    while True:
        resp = input('Quer continuar ? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Opção inválida. Digite somente S ou N.')
    if resp in 'Nn':
        break
print('-='*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
print('-='*30)
print(f'O jogador {dados["jogador"]} jogou {partidas}.')
for p in range (0, len(lista)) :
    print(f'Na partida {p}, fez {lista[p]} gols.')
print(f'Foi um total de {dados["total"]} gols.')
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["jogador"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print(' <<VOLTE SEMPRE>> ')