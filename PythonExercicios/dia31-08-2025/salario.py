valor_hora = float(input("Digite o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.09
desconto_sindicato = salario_bruto * 0.04

total_descontos = desconto_ir + desconto_inss + desconto_sindicato


salario_liquido = salario_bruto - total_descontos

print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto IR (11%): R$ {desconto_ir:.2f}")
print(f"Desconto INSS (9%): R$ {desconto_inss:.2f}")
print(f"Desconto Sindicato (4%): R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

