"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
"""
frase = input("Digite um frase qualquer: ")
print(f"Palindromo: {frase.replace(' ', '').lower() == frase[::-1].replace(' ', '').lower()}")
print(f"normal: {frase}")
print(f"ao contrário: {frase[::-1]}")
