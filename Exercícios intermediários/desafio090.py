situacao = {}
situacao['nome'] = input('Nome do aluno: ')
situacao['média'] = float(input('Média do aluno:'))
if situacao['média'] < 7:
    situacao['situacao'] = 'Reprovado'
else:
    situacao['situacao'] = 'Aprovado'
for n, m in situacao.items():
    print(f'O {n} é {m}')
