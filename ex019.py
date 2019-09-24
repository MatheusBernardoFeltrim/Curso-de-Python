import random
n1 = input('Escreva o nome do seu aluno')
n2 = input('Escreva o nome de seu aluno')
n3 = input('Escreva o nome de seu aluno')
n4 = input('Escreva o nome do seu aluno')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print ('o Aluno escolido foi {}'.format(escolhido))