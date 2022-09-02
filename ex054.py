"""
Crie um programa que leio o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.
"""
from datetime import datetime
ANO = datetime.now().year
maiores = menores = 0
for x in range(1, 8):
    nasc = int(input(f"Digite a idade da {x}º pessoa: "))
    idade = ANO - nasc
    print(f"({idade} anos de idade)\n")
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f"\nTotal de pessoas:\n"
      f"Maiores de 18 anos: {maiores}\n"
      f"Menores de 18 anos: {menores}")
