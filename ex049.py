"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""
num = int(input("Digite um número inteiro que você deseja ver a tabuada: "))

for x in range(1, 11):
    print(f"{num} x {x} = {num * x}")
