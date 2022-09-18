#Ex:

salario_mensal = float(input("Digite o valor do seu salário: "))
gasto_mensal = float(input("Digite o gasto mensal: "))

salario_Total = salario_mensal*12
gasto_total = gasto_mensal * 12

montante_economizado = salario_Total-gasto_total

print(f"O montante previsto para o fim do ano é de:\n{montante_economizado}")

