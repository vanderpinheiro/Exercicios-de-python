import random
a = input('Digite o nome do aluno:')
b = input('Próximo:')
c = input('Próximo:')
d = input('Último:')
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem escolhida dos alunos foi:')
print(lista)