b = float(input('Qual é a largura da parede?'))
h = float(input('Qual é a algura da parede?'))
area= b*h
tinta = area/2

print ('Para pintar uma parede de {}m², considerando que 1l de tinta pinta 2m²,\n'
       ' a quantidade em litros de tinta necessárias será {}l de tinta.'.format(area,tinta))
