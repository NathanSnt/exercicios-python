"""
Faça um programa que mostre a tabuaada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o valor solicitado for negativo.
"""
while True:
    num = int(input("Digite um número inteiro que deseja ver a tabuada: "))
    if num < 0:
        break
    print("="*15)
    for x in range(1, 11):
        print(f"{num} x {x} = {num*x}")
    print("=" * 15)
