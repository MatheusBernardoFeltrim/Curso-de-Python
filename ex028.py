import random
m = random.randint(1,5)
n = int(input('Adivinhe o numero que o computador escolher entre 1 e 5 '))
if m==n:
    print('Você acertou!')
else:
    print('Você Errou,Tente novamente!')
print('O numeiro que o computador escolheu foi {}'.format(m))
print('======Fim=======')
