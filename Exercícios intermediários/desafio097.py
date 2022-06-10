def msg(txt):
    a = len(txt) +4
    print('~'*(a))
    print(f'  {txt}')
    print('~'*(a))
    return a

    #cód principal
b = msg('  Aprenda python maneirinho  ')
print(b)