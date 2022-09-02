"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot

cat_opo = float(input("Digite o valor do cateto oposto: "))
cat_adj = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = hypot(cat_opo, cat_adj)
print(f"O valor da hipotenusa é igual a {hipotenusa:.2f}")
