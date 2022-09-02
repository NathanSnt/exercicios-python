"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.
"""
num1 = int(input("Digite um número inteiro qualquer: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 != num2:
    print(f"O {'primeiro'if num1 > num2 else 'segundo'} valor é o maior")
else:
    print(f"Não existe valor maior, os dois são iguais.")
