nome = input()
salario = float(input())
montante_vendas = float(input())

comissao = montante_vendas * 0.15
salario_total = salario + comissao

print(f"TOTAL = R$ {salario_total:.2f}")