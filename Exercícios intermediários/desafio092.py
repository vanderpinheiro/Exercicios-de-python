import datetime
dados = {}
dados['nome']= input('Nome: ')
nasci = int(input('Ano de nascimento: '))
dados['idade']= datetime.date.today().year - nasci
CTPS= int(input('Carteira de Trabalho (0 não tem):'))
if CTPS == 0:
    dados['CTPS']= 0
elif CTPS > 0:
    dados['CTPS']=CTPS
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratação'] + 35) - nasci
print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')