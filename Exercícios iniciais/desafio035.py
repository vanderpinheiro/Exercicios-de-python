r = float(input('Digite tamanho da reta r:'))
s = float(input('Digite tamanho da reta s:'))
t = float(input('Digite tamanho da reta t:'))
if r < (s+t) and s < (r+t) and t < (r+s):
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo')