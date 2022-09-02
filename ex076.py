"""
Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
produtos = ("Televisão de plasma", 800.90,
            "Janela de alumínio", 5000,
            "Bicicleta", 2533,
            "Saco de café tropeiro", 49.99,
            "Banco de praça", 73,
            "Notebook Positivo", 2350,
            "Mouse pad CS GO", 55,
            "Terno preto", 900)
print(f"{'PRODUTO':^30}|{'PREÇO':^10}")
print("-"*40)
for x in range(0, len(produtos), 2):
    print(f"{produtos[x]:.<30}R${produtos[x+1]:>8.2f}")
