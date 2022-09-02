"""
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
pa = a1 = int(input("Digite o valor do primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
x = 0
while x != 10:
    print(pa)
    pa += razao
    x += 1

opc = 1
while opc != 0:
    opc = int(input("Quantos mais termos você deseja ver? "))
    for x in range(opc):
        print(pa)
        pa += razao
print("Até mais.")
