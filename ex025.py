"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = input("Digite o seu nome completo: ")
if "silva" in nome.lower():
    print(f"Você TEM SILVA no seu nome.")
else:
    print("Você NÃO tem SILVA no seu nome.")
