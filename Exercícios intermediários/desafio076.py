lista = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estejo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

for pos,t in enumerate(lista):
    if pos%2 == 0:
        print('{:.<30}'.format(t),end='')
    else:
        print('R${:>7.2f}'.format(t))
