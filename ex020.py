"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle

aluno1 = input("Digite o nome do aluno 1: ")
aluno2 = input("Digite o nome do aluno 2: ")
aluno3 = input("Digite o nome do aluno 3: ")
aluno4 = input("Digite o nome do aluno 4: ")
ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)

print(f"A ordem de apresentação é: {ordem}")
