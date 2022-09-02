"""
Desenvolva um programa que leia o primeiro termo e a razão de um PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
termo = int(input("Digite o primeiro termo da PA: "))
rz = int(input("Digite a razão da PA: "))

for x in range(1, 11):
    print(termo)
    termo += rz
