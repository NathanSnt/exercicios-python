"""
Crie um programa que faça o computador jogar jokempô com você.
"""
from random import randint
from time import sleep
jogo = ("PEDRA", "PAPEL", "TESOURA")

opc = jogo[int(input("Sua escolha:\n"
                     "[1] PEDRA\n"
                     "[2] PAPEL\n"
                     "[3] TESOURA\n"
                     ">>> "))-1]
computador = jogo[randint(0, 2)]

jokenpo = 'JO KEM PÔ'
for x in jokenpo:
    print(x, end='', flush=True)
    sleep(0.2)
print(end="\n\n")

if opc == computador:
    print("EMPATE!")
elif opc == "PEDRA":
    if computador == "PAPEL":
        print("O COMPUTADOR GANHOU!!")
    elif computador == "TESOURA":
        print("VOCÊ GANHOU!!")
elif opc == "PAPEL":
    if computador == "PEDRA":
        print("VOCÊ GANHOU!!")
    elif computador == "TESOURA":
        print("O COMPUTADOR GANHOU!!")
elif opc == "TESOURA":
    if computador == "PEDRA":
        print("O COMPUTADOR GANHOU!!")
    elif computador == "PAPEL":
        print("VOCÊ GANHOU!!")
print(f"Você jogou {opc} e o computador jogou {computador}.")
