dis ={}
def notas(*num,sit=True):
    maior=menor=0
    situac=''
    total = len(num)
    for c in range(0,len(num)):
        if c == 0:
            maior = num[0]
        elif maior < num[c]:
            maior = num[c]
    for c in range (0,len(num)):
        if c == 0:
            menor = num[0]
        elif menor > num[c]:
            menor = nun[c]
    média = sum(num)/len(num)
    if média >= 7:
        situac = 'BOA'
    elif 5<=média<7:
        situac = 'MÉDIA'
    else:
        situac = 'RUIM'
    dis['total'] = total
    dis['maior'] = maior
    dis['menor'] = menor
    dis['média'] = média
    if sit == True:
        dis['situação=']=situac

    return dis


resp = notas(3,5,7,8,9,4,sit=True)
print(resp)