"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
- O programa deverá escrever na tela se o usuário ganho ou perdeu.
"""
from random import randint

computador = randint(0, 5)

print("Pensei em um número entre 0 e 5, tente adivinhar qual foi.")
chute = int(input("Seu chute >>> "))

if -1 < chute < 6:
    if chute == computador:
        print("PARABÉNS!!")
        print(f"O número que eu pensei era exatamente o {computador}")
    else:
        print("Você errou!")
        print(f"O número que eu tinha pensado era o {computador}")
else:
    print("Seu chute tem que ser um número entre 0 e 5.")
