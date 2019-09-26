v = int(input('Quantos K/H esta o seu carro? '))
if v>80:
    m = (v-80)*7
    print('Você foi mutado, e tera que pagar R${:.2f} de multa'.format(m))
else:
    print('Digija com cudado')