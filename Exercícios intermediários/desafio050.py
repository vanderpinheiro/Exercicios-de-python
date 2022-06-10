w = 0
for c in range(1,7):
    p = int(input('Digite um número:'))
    if p % 2 == 0:
        w = p + w
print(w)