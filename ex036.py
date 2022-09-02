"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.
A prestação mensal, nõa pode exceder 30% do salário ou então o empréstimo será negado.
"""
valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
anos_pagar = int(input("Em quantos anos será pago: "))

mensalidade = (valor_casa / anos_pagar) / 12
maximo = salario * (30 / 100)

if mensalidade > maximo:
    print(f"EMPRÉSTIMO NEGADO!\n"
          f"Mensalidade: R${mensalidade:.2f}\n"
          f"Salário: R${salario:.2f}\n"
          f"Dividido em {anos_pagar} anos")
else:
    print(f"EMPRÉSTIMO APROVADO!\n"
          f"Mensalidade: R${mensalidade:.2f}\n"
          f"Salário: R${salario:.2f}\n"
          f"Dividido em {anos_pagar} anos")
