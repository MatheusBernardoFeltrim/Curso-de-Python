n = int(input('Digite o numeiro de dias que ficou com o carro'))
n1 = float(input('Digite quantos km percorridos com o carro'))

v = (n*60)+(n1*0.15)

print('O total a pagar é de R${}'.format(v))
