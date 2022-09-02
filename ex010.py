"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere:
US$ 1,00 = 3,27
"""
DOLAR = 3.27
real = float(input("Digite o valor que voce tem em carteira: R$"))
dolar = real / DOLAR

print(f"Com R${real:.2f} voce consegue comprar US${dolar:.2f}")
