entrada1 = input()
valores1 = entrada1.split()
peca1 = int(valores1[0])
num_pecas1 = int(valores1[1])
valor_peca1 = float(valores1[2])

entrada2 = input()
valores2 = entrada2.split()
peca2 = int(valores2[0])
num_pecas2 = int(valores2[1])
valor_peca2 = float(valores2[2])

valor_total = (num_pecas1 * valor_peca1) + (num_pecas2 * valor_peca2)
print(f'VALOR A PAGAR: R$ {valor_total:.2f}')