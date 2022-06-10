lista = []
while True:
    lista.append(int(input('Digite um valor para adicionar a lista: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp in 'Nn':
        break
a = []
b = []
print(len(lista))
pos = 0
while pos < len(lista):
    if lista[pos]%2 == 0:
        a.append(lista[pos])
    else:
        b.append(lista[pos])
    pos += 1
print(a)
print(b)