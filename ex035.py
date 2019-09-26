l1 = float(input("primeiro segmento"))
l2 = float(input('Segundo segmento'))
l3 = float(input('terceiro segmento'))
if l1 <l2 + l3 and l2< l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMA UM TRIÂNGULO')
else:
    print('OS segmentos acima NÃO PODEM FORMA UM TRIÂNGULO')

