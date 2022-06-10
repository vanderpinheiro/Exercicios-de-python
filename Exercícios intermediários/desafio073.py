times = ('Corinthians','Bragantino','Atlético-MG','Santos','Coritiba','Cuiabá','Internacional','Avaí','América-MG'
         ,'Palmeiras','Flamengo','Botafogo','São Paulo','Fluminense','Ceará SC','Athletico-PR','Atlético-GO','Goiás'
         ,'Juventude','Fortaleza')
print('-='*15)
for t in times:
    print(t)
print('-='*15)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('-='*15)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('-='*15)
print(f'os times em ordem Alfabética: {sorted(times)}')
print('-='*15)
time = input('Digite um time para saber sua posição na tabela: ')
print(f'O time {time} está na {times.index(time)+1}ª posição')