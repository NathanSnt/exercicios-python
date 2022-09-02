"""
Crie um programa quee crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
lista = [[], [], []]
for x in range(3):
    for y in range(3):
        lista[x].append(int(input(f"Digite um valor para a posição [{x},{y}]: ")))

for x in range(3):
    for y in range(3):
        print(f"[ {lista[x][y]} ]", end=" ")
    print()
