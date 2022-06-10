a = float(input('Digite a primeira reta:'))
b = float(input('Digite a segunda reta:'))
c = float(input('Digite a terceira reta:'))
if a + b > c and b + c > a and a + c > b:
    print('Estas retas podem formar um triângulo')
    if a == b and b == c and c == a:
        print('Este triângulo é equilátero.')
    elif a == b or a == c or c == b:
        print('Este triângulo é isósceles.')
    else:
        print('Este trigângulo é escaleno')
else:
    print('Essas retas não podem formar um triângulo')
