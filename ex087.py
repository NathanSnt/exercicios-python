"""
Aprimore o desafio anterior, mostrando no final:
- A soma de todos os valores pares digitados
- A soma dos valores da terceira coluna
- O maior valor da segunda linha
"""
lista = [[], [], []]
tot = soma3 = maior = 0
for x in range(3):
    for y in range(3):
        lista[x].append(int(input(f"Digite um valor para a posição [{x},{y}]: ")))

for x in range(3):
    for y in range(3):
        if lista[x][y] % 2 == 0:
            tot += lista[x][y]
        if y == 2:
            soma3 += lista[x][y]
        print(f"[ {lista[x][y]} ]", end=" ")
    print()
maior = max(lista[1])

print(f"\nSoma de todos valore pares: {tot}\n"
      f"Soma dos valores da terceira coluna: {soma3}\n"
      f"Maior valor da segunda linha: {maior}")
