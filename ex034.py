"""
Esccreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input("Digite o valor do salário do funcionáro: R$"))

if salario > 1250:
    percent = 10 / 100
    aumento = salario * percent
    novo_salario = salario + aumento
else:
    percent = 15 / 100
    aumento = salario * percent
    novo_salario = salario + aumento

print(f"Salário antigo: R${salario:.2f}\n"
      f"Novo salário: R${novo_salario:.2f}\n"
      f"Aumento de R${aumento:.2f}. {percent * 100:.0f}% do salário antigo.")
