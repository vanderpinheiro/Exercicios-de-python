nome = input('Qual o nome do aluno?')
a = float(input('Digite a primeira nota:'))
b = float(input('Digite a segunda nota:'))
media = (a+b)/2

if media < 5:
    print('O aluno {} obteve média final {}. FOI \033[4:31:40mREPROVADO\033[m'.format(nome,media))
elif 5 <= media <= 6.9:
    print('O aluno {} obteve média final {}. ESTÁ DE \033[4::43mRECUPERAÇÃO\033[m'.format(nome, media))
else:
    print('O aluno {} obteve média final {}. ESTÁ \033[4::46mAPROVADO0\033[m'.format(nome, media))