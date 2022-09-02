"""
Faça um programa que leia um frase pelo teclado e mostre:
- Quanta vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez
"""
frase = input("Digite uma frase qualquer: ")
print(f"A letra 'A' apareceu {frase.lower().count('a')} vezes na frase digitada")
print(f"A primeira ocorrência foi na posição {frase.lower().find('a')}")
print(f"A última ocorrência foi na posição {frase.lower().rfind('a')}")
