lista = []
while True:
    c = int(input('Digite um valor: '))
    lista.append(c)
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp in 'Nn':
         break
print(f'Fora digitados {len(lista)} números na lista')
lista.sort(reverse=True)
print(f'A lista em forma decrescente é {lista}')
c = lista.count(5)
if c == 0:
     print('O número 5 não está na lista')
else:
     print(f'O número 5 está na lista e aparece {c} vezes')