from random import shuffle
n1 = str(input('Primeiro aluno'))
n2 = input('segundo aluno')
n3 = input ('Terceira Aluno')
n4 = input ('Quarto aluno')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print (lista)
