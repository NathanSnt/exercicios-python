"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
"""
media = mulher_menos_20 = velho = 0
homem_velho = ''

for x in range(1, 5):
    nome = input(f"Digite o nome da {x}º pessoa: ")
    idade = int(input(f"Digite a idade: "))
    sexo = input("Sexo da pessoa [M/F] ").upper()
    if idade > velho and sexo == "M":
        homem_velho = nome
    if sexo == "F" and idade < 20:
        mulher_menos_20 += 1
    media += idade
media /= 4

print(f"\nMédia de idade do grupo: {media:.1f}\n"
      f"Nome do homem mais velho: {homem_velho}\n"
      f"Mulheres com menos de 20: {mulher_menos_20}")
