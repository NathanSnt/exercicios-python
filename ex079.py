"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente.
"""
lista = []
while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado.")
    else:
        print("Valor já existente na lista.")
    cont = input("Continuar? [S/n] ").upper()
    if cont == "N":
        break
print(f"Lista ordenada em ordem crescente: {sorted(lista)}")
