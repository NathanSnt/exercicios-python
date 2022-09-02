"""
Crie um programa que leia o nome completo de uma pesssoa e mostre:
- O nome com todas as letras maiúculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerear espaços)
- Quantas letras tem o primeiro nome
"""
nome = input("Digite o seu nome completo: ")
print(f"Nome completo: {nome}")
print(f"Nome em maiúsculo: {nome.upper()}")
print(f"Nome em minúsculo: {nome.lower()}")
print(f"Total de letras (sem contar espaços): {len(nome.replace(' ', ''))}")
print(f"Total de letras no primeiro nome: {len(nome.split()[0])}")
