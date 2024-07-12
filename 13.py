import math
entrada = input()
valores = entrada.split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
maior_AB = (a + b + abs(a - b)) / 2
maior = (maior_AB + c + abs(maior_AB - c)) / 2
print('%d eh o maior' % maior)