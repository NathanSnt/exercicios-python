"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""
nome = input("Digite o seu nome completo: ")
print(f"Nome completo: {nome.title()}")
print(f"Primeiro nome: {nome.split()[0].capitalize()}")
print(f"Ultimo nome: {nome.split()[-1].capitalize()}")
