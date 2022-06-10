'''nome = input('Digite seu nome completo:').strip()
nome= nome.upper()
c = nome.find('SILVA')
print('Seu nome tem Silva?', c!=-1 )'''

nome = input('Digite seu nome completo:').strip()
print("Seu nome tem Silva? {}".format('silva' in nome.lower()))