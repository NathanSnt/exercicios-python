"""
Faça um programa que ajude o jogador da MEGA-SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import sample
jogos = []
for x in range(int(input("Quantos jogos você deseja gerar? "))):
    jogos.append(sample(range(1, 60), 6))

    print("-"*35)
    print(f"Jogo {x+1}: {jogos[x]}")
