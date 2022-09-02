"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input("Digite o salário do funcionário R$: "))
novo_salario = salario + (salario * (15 / 100))

print(f"O novo salário do funcionário com 15% de aumento é de R${novo_salario:.2f}")
