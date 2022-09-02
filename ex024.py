"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".
"""
nome = input("Digite o nome de uma cidade: ")
if "santo" == nome.split()[0].lower():
    print(f"A cidade {nome} TEM 'SANTO' no começo do nome.")
else:
    print(f"A cidade {nome} NÃO TEM 'SANTO' no começo do nome.")
