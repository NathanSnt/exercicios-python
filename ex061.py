"""
Refaça od desafio 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiro termos da progressão
usando a estrutura de repetição while.
"""
pa = a1 = int(input("Digite o valor do primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
x = 0
while x != 10:
    print(pa)
    pa += razao
    x += 1
