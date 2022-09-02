"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiro elemnentos de uma sequência de fibonacci.
"""
n = int(input("Quantos elementos de fibonacci deseja ver: "))
x = 0
aux1 = aux2 = 0
f = 1
while x != n:
    print(aux1, end=' -> ') if x != n-1 else print(aux1)
    aux2 = aux1
    aux1 = f
    f += aux2
    x += 1
