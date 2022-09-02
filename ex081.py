"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
- Quantos números foram digitados.
- A lista de valores, ordenada de forma decrescente.
- Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    lista.append(int(input("Digite um valor: ")))

    parar = input("Continuar? [S/n] ").upper()
    if parar == "N":
        break

print(f"Foram digitados {len(lista)} valores.\n"
      f"Lista ordenada decrescentemente: {sorted(lista, reverse=True)}.\n"
      f"O valor 5", end=' ')
if 5 in lista:
    print(f"está na lista, na posição {lista.index(5)}.")
else:
    print("não está na lista.")
