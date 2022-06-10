import math
ang = float(input('Digite um ângulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O seno, cosseno e tangente deste ângulo é, consecutivamente:{:.2f}, {:.2f}, {:.2f}'.format(sen,cos,tg))