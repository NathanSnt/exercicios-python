"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilatero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes
"""
r1 = int(input("Digite o valor da reta 1: "))
r2 = int(input("Digite o valor da reta 2: "))
r3 = int(input("Digite o valor da reta 3: "))

t = False

if (r1 - r2) < r3 < r1 + r2:
    if (r3 - r2) < r1 < r3 + r2:
        if (r3 - r1) < r2 < r3 + r1:
            t = True

if r1 == r2 and r2 == r3:
    tipo = 'equilátero'
elif r1 == r2 or r1 == r3 or r2 == r3:
    tipo = 'isósceles'
else:
    tipo = 'escaleno'

if t:
    print(f"Dá para formar um triângulo {'do tipo ' + tipo} com essas retas.")
else:
    print(f"Essas retas não conseguem formar um triângulo.")
