"""
Faça um programa para jogar par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
"""
from random import randint
from time import sleep
vitorias = 0
while True:
    opc = input("Par ou ímpar? [P/I]")[0].upper()
    if opc not in ("P", "I"):
        print("Opção inválida!")
    else:
        print("PAR")
        sleep(1)
        print("OU")
        sleep(1)
        print("ÍMPAR")
        sleep(1)
        num = int(input(">>> "))
        computador = randint(0, 5)
        resultado = num + computador
        if resultado % 2 == 0:
            if opc == "P":
                print(f"você: {num} | computador: {computador} ")
                print(f"{num} + {computador} = {resultado} que é {'ímpar' if resultado % 2 != 0 else 'par'}.")
                print("Você Ganhou!!!")
            else:
                print(f"você: {num} | computador: {computador} ")
                print(f"{num} + {computador} = {resultado} que é {'ímpar' if resultado % 2 != 0 else 'par'}.")
                print("O Computador Ganhou.")
                print("Fim de jogo.")
                break
        else:
            if opc == "I":
                print(f"você: {num} | computador: {computador} ")
                print(f"{num} + {computador} = {resultado} que é {'ímpar' if resultado % 2 != 0 else 'par'}.")
                print("Você Ganhou!!!")
            else:
                print(f"você: {num} | computador: {computador} ")
                print(f"{num} + {computador} = {resultado} que é {'ímpar' if resultado % 2 != 0 else 'par'}.")
                print("O Computador Ganhou.")
                print("Fim de jogo.")
                break
        vitorias += 1
        print("vamos jogar denovo... \n")
print(f"\nVitórias consecutivas: {vitorias}")
