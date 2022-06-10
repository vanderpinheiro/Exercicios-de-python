pt = int(input('Informe o primeiro termo da PA: '))
q = int(input('Informe a razão da PA: '))
pulo = pt + (10-1)*q
for c in range(pt, pulo+q, q):
    print(c, end=' → ')