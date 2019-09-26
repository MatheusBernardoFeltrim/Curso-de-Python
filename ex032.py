from datetime import date
a = int(input('Qual ano vc quer analisar?Coloque 0 analisar o ano atual'))
if a == 0:
    a = date.today().year
if a % 4 ==0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(a))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(a))
