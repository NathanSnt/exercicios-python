"""
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram
no intervalo de 1 até 500.
"""
tot = 0
for x in range(1, 501):
    if x % 2 != 0 and x % 3 == 0:
        tot += x
print("A soma de todos número inpares que são divisiveis por três e que se encontram no interevalo entre 1 e 500:\n"
      f"Total = {tot}")
