dados ={}
lista=[]
c = 0
dados['jogador'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
for p in range (0,partidas):
    lista.append( int(input(f'Quantos gols na partida {p+1}?')))
dados['gols'] = lista[:]
'''for p in range (0,len(lista)):
    c +=lista[p]'''

dados['total'] = sum(lista)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O {k} tem como valor {v}. ')
print('-='*30)
print(f'O jogador {dados["jogador"]} jogou {partidas}.')
for p in range (0, len(lista)) :
    print(f'Na partida {p}, fez {lista[p]} gols.')
print(f'Foi um total de {dados["total"]} gols.')