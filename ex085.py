"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.
"""
lista = [[], []]
for x in range(7):
    num = int(input(f"Digite o {x+1}º valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f"\nValores pares: {sorted(lista[0])}")
print(f"Valores ímpares: {sorted(lista[1])}")
