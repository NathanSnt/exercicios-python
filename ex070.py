"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
- Qual é o total de gasto na compra.
- Quantos produtos custam mais de R$1.000,00.
- Qual é o nome do produto mais barato.
"""
tot = mais_mil = barato_valor = 0
barato_nome = ''
print("="*30)
print(f"{'MERCADÃO DA VILA':^30}")
print("="*30)
while True:
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor R$ "))
    if tot == 0:
        barato_nome = nome
        barato_valor = valor
    tot += valor
    if valor > 1000:
        mais_mil += 1
    if valor < barato_valor:
        barato_nome = nome
        barato_valor = valor

    cont = input("Continuar adicionando produtos? [S/n] ").upper()
    if cont == "N":
        break

print("\n\n")
print(f"{' FECHAMENTO ':=^40}")
print(f"Total de gasto: R${tot:.2f}\n"
      f"Produtos acima de R$1.000,00: {mais_mil}\n"
      f"Produto mais barato: {barato_nome} | R${barato_valor:.2f}")
