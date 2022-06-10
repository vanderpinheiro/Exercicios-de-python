import math
cat1= float(input('Digite um dos lados do triângulo:'))
cat2= float( input('Digite o outro lado do triângulo:'))
'''hip= math.sqrt(pow(cat1,2)+pow(cat2,2,))
print('O valor da hipotenusa é: {}'.format(hip))'''
hip = math.hypot(cat1, cat2)
print('O valor da hipotenusa é: {}'.format(hip))