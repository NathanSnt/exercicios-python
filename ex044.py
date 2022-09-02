"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e a condição de pagamento:
- Á vista no dinheiro ou cheque:
    10% de desconto
- Á vista no cartão:
    5% de desconto
- Em até 2x no cartão:
    preço normal
- 3x ou mais no cartão:
    20% de juros
"""
produto = float(input("Digite o valor do produto: R$"))
print("Escolha a forma de pagamento: \n"
      "[1] DINHEIRO\n"
      "[2] CHEQUE\n"
      "[3] CARTÃO\n")
opc = int(input(">>> "))

if opc == 1:
    desconto = produto * (10 / 100)
    valor = produto - desconto
    print(f"Valor do produto: R${produto:.2f}\n"
          f"Desconto aplicado: R${desconto:.2f}\n"
          f"Valor a pagar: R${valor:.2f}\n\n"
          f"Forma de pagamento escolhido: DINHEIRO")
elif opc == 2:
    desconto = produto * (10 / 100)
    valor = produto - desconto
    print(f"Valor do produto: R${produto:.2f}\n"
          f"Desconto aplicado: R${desconto:.2f}\n"
          f"Valor a pagar: R${valor:.2f}\n\n"
          f"Forma de pagamento escolhido: CHEQUE")
elif opc == 3:
    parcelado = int(input("Em quantas vezes? "))
    if parcelado == 1:
        desconto = produto * (5 / 100)
        valor = produto - desconto
        print(f"Valor do produto: R${produto:.2f}\n"
              f"Desconto aplicado: R${desconto:.2f}\n"
              f"Valor a pagar: R${valor:.2f}\n\n"
              f"Forma de pagamento escolhido: CARTÃO Á VISTA")
    elif parcelado == 2:
        valor = produto
        print(f"Valor do produto: R${produto:.2f}\n"
              f"Desconto aplicado: R${0},00\n"
              f"Valor a pagar: R${valor:.2f}\n\n"
              f"Forma de pagamento escolhido: 2X NO CARTÃO")
    elif parcelado >= 3:
        juros = produto * (20 / 100)
        valor = produto + juros
        print(f"Valor do produto: R${produto:.2f}\n"
              f"Juros aplicado: R${juros:.2f}\n"
              f"Valor a pagar: R${valor:.2f}\n\n"
              f"Forma de pagamento escolhido: {parcelado}X NO CARTÃO")
    else:
        print("Erro inesperado.")
else:
    print("opção inválida!")
