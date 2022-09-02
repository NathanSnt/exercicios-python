"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
"""
num = int(input("Digite um número que você deseja ver o fatorial: "))
fatorial = 1
x = num
while x != 0:
    fatorial *= x
    x -= 1
"""
for x in range(num, 0, -1):
    fatorial *= x
"""
print(f"{num}! = {fatorial}")
