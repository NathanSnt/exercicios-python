"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
- Quantas pessoas foram cadastradas.
- Uma listagem com as pessoas mais pesadas.
- Uma listagem com as pessoas mais leves.
"""
lista = []
while True:
    nome = input("Digite o nome: ")
    peso = float(input(f"Digite o peso de {nome}: "))
    lista.append([nome, peso])

    parar = input("Deseja continuar? [S/n] ").upper()
    if parar == "N":
        break

leve = pesado = lista[0][1]
for pessoa in lista:
    if pessoa[1] > pesado:
        pesado = pessoa[1]
    if pessoa[1] < leve:
        leve = pessoa[1]

print(f"\nForam lidos dados de {len(lista)} pessoas\n"
      f"Listagem das pessoas mais pesadas ({pesado:.1f}kg): ", end='')
for pessoa in lista:
    if pessoa[1] == pesado:
        print(f"{pessoa[0]}", end="... ")

print('')

print(f"Listagem das pessoas mais leves ({leve:.1f}kg): ", end='')
for pessoa in lista:
    if pessoa[1] == leve:
        print(f"{pessoa[0]}", end="... ")
