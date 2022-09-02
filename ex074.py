"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o maior e o menor valor que estão na tupla.
"""
from random import randint
tupla = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f"Tupla: {tupla}\n"
      f"Maior: {max(tupla)}\n"
      f"Menor: {min(tupla)}")
