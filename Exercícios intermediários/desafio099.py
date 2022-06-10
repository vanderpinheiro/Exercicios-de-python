import time
def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    c = 0
    if len(num)>=1:
        print('Os números digitados foram : ', end='')
        for p in (num):
            print(f'{p}', end=' ')
            time.sleep(1)
        print('')
        print(f'Foram informados {len(num)} valores ao todo.')
        for p in num:
            if p > c:
             c = p
        print(f'O maior valor informado foi {c} ')
    elif len(num)==0:
        print('Você não informou nenhum valor.')

maior(7,2,6,1)

maior(1)
