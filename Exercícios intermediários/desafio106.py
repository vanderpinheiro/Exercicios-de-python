def ajuda():
    import time
    what = str(input('Função ou Biblioteca > '))
    print('\033[0;0;41m~'*(34+len(what)))
    print(f'  Acessando o manual do comando {what}')
    print('~'*(34+len(what)))
    time.sleep(1)
    print('\033[m')
    help(what)
    return what

while True:
    resp = ajuda()
    print(resp)
    if resp == 'fim'.strip().lower():
        break