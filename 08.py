num_funcionario = int(input())
horas_trabalhadas = int(input())
salario_hora = float(input())

valor_salario = horas_trabalhadas * salario_hora
print("NUMBER =", num_funcionario)
print(f"SALARY = U$ {valor_salario:.2f}")