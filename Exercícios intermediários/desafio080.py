valores = []
for cont in range (0,5):
    c = int(input('Digite um valor: '))
    if cont == 0 or c > valores[-1]:
        valores.append(c)
    else:
        pos = 0
        while pos < len(valores):
            if c <= valores[pos]:
                valores.insert(pos,c)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos +=1

print(valores)