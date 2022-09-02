"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente
"""
alunos = []
while True:
    nome = input("Digite o nome do aluno: ")
    notas = [float(input("nota 1: ")), float(input("nota 2: "))]
    alunos.append([nome, notas])

    parar = input("Deseja continuar? [S/n] ").upper()
    if parar == "N":
        break

print(f"{'ID':<3}|{'NOME DO ALUNO':^20}|{'MÉDIA':^10}")
for aluno in alunos:
    print(f"{alunos.index(aluno):<3}|{aluno[0]:^20}|{sum(aluno[1])/2:^10.1f}")

while True:
    ver = int(input("Deseja ver as notas de qual aluno (999 para parar): "))
    if ver == 999:
        break
    print("-"*30)
    print(f"notas do aluno {alunos[ver][0]}: {alunos[ver][1]}")
    print("-"*30)
