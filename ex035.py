"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
r1 = int(input("Digite o valor da reta 1: "))
r2 = int(input("Digite o valor da reta 2: "))
r3 = int(input("Digite o valor da reta 3: "))

t = False

if (r1 - r2) < r3 < r1 + r2:
    if (r3 - r2) < r1 < r3 + r2:
        if (r3 - r1) < r2 < r3 + r1:
            t = True
if t:
    print(f"Dá para formar um triângulo com essas retas.")
else:
    print(f"Essas retas não conseguem formar um triângulo.")
