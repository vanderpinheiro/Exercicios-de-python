import random
import time
jogos = {}
jogos['jogador1'] = random.randint(1,6)
jogos['jogador2'] = random.randint(1,6)
jogos['jogador3'] = random.randint(1,6)
jogos['jogador4'] = random.randint(1,6)
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
    time.sleep(1)

print('Ranking dos jogadores:')
for i in sorted(jogos, key= jogos.get,reverse=True):
    print(i, jogos[i])
    time.sleep(1)