v = int(input('Digite o tamanho em km da sua viagem'))
if v<200:
    v1 = (v*0.5)
else:
    v1 = (v*0.45)
print('Sua viagem vai custar R${:.2f}'.format(v1))