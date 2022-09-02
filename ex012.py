"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
produto = float(input("Digite o preço do produto: R$"))
novo_preco = produto - (produto * (5 / 100))

print(f"O novo valor do produto com 5% de desconto é de R${novo_preco:.2f}")
