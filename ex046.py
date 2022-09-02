"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
for x in range(10, 0, -1):
    print(f"{x}", end='.. ')
    sleep(1)
print("FELIZ ANO NOVO!!")
