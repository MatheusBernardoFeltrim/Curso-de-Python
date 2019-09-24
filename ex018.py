import math
n = int(input('Digite um ângulo qualquer'))
c = math.cos(n)
s = math.sin(n)
t = math.tan(n)

print('o seno do ârgulo {} é {:.2f},o cosseno é {:.2f} e a tangente é {:.2f}'.format(n, s, c, t))
