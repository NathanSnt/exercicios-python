"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
lista = []
for x in range(5):
    num = int(input(f"Digite o {x+1}º valor: "))
    if x == 0:
        lista.append(num)
        print("Valor adicionado na lista.")
    if num > lista[-1]:
        lista.append(num)
        print(f"Valor adicionado no final da lista.")
    for y in lista:
        if num < y:
            lista.insert(lista.index(y), num)
            print(f"Valor adicionado na posição {lista.index(y)}.")
            break
print(f"\nLista em ordem: {lista}")
