"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ela.
"""
algo = input("Digite algo: ")
print(f"Tipo primitivo: {type(algo)}")
print(f"tamanho: {len(algo)}")
print(f"É alfabético: {algo.isalpha()}")
print(f"É alfanumérico: {algo.isalnum()}")
print(f"É um número: {algo.isdigit()}")
print(f"Só tem espaços: {algo.isspace()}")
print(f"Esta em maiúsula: {algo.isupper()}")
print(f"Esta em minúscula: {algo.islower()}")
print(f"Esta capitalizada: {algo.istitle()}")