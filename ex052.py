"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num = int(input("Digite um número inteiro qualquer: "))
primo = True
for x in range(num-1, 1, -1):
    if num % x == 0:
        primo = False
if primo:
    print(f"O número {num} É um número primo.")
else:
    print(f"O número {num} NÃO é um número primo.")
