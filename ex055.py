"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido
"""
for x in range(1, 6):
    peso = float(input(f"Digite o peso da {x}º pessoa: "))
    if x == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"O maior peso lido foi de {maior:.2f}kg\n"
      f"O menor peso lido foi de {menor:.2f}kg")
