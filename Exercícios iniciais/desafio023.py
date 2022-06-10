num = int(input('Digite um número de 0 a 9999:'))
cores = {
    'limpa':'\033[m',
    'azul':'\033[0;36;40m',
    'vermelho':'\033[4;31;40m'
}
u = num%10
d = num//10%10
c = num//100%10
m = num//1000%10
print('Analisando o número {}'.format(num))

print('Unidade {}{}{}'.format(cores['azul'],u, cores['limpa]))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))
