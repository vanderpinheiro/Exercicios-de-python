lista = []
nomeenotas = [[],[],[]]
d = 0
while True:
    nome  = input('Digite o nome do aluno: ')
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota2+nota1)/2
    lista.append([nome,[nota1,nota2],media])
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp in 'Nn':
        break
print(lista)
