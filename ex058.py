"""
Melhore o jogo do desafio 028 onde o computador "pensa" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
chutes = 1
computador = randint(0, 10)
chute = computador + 1
print("Pensei em um número entre 0 e 10, tente adivinhar qual foi.")
while chute != computador:
    chute = int(input("Seu chute: "))
    chutes += 1
    if chute != computador:
        print("Errou, tente novamente\n")
print("\nPARABÉNS VOCE ACERTOU!")
print(f"você precisou de {chutes} tentativas para descobrir")
