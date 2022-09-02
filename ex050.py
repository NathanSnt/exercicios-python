"""
Desenvolva um programa que leia seis números inteiros e mostra a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o.
"""
tot = 0
for x in range(1, 7):
    y = int(input(f"Digite o {x}º número: "))
    if y % 2 == 0:
        tot += y
print(f"A soma de todos os número pares digitados é igual a {tot}")
