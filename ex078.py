"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []
pares = []
impares = []

for x in range(5):
    lista.append(int(input(f"Digite o {x+1}º valor: ")))

print(f"Lista complete: {lista}\n"
      f"Maior valor: {max(lista)} na {lista.index(max(lista))+1}º posição.\n"
      f"Menor valor: {min(lista)} na {lista.index(min(lista))+1}º posição.")
