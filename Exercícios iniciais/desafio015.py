d = int(input('Por quantos dias o carro foi alugado?'))
km = float (input('Quantos quilômetros foram rodados?'))
custo = (d*60)+(km*0.15)
print('O preço a pagar pelo aluguel do carro será de R${:.2f}'.format(custo))