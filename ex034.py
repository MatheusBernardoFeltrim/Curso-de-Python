s = float(input('Digite o seu salário'))
if s> 1250 :
    s1 = (s*1.1)
else:
    s1 = (s*1.15)
print('o seu salário atual é de R${}'.format(s1))
