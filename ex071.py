"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possua cédulas de R$50, R$20, R$10 e R$1.
"""
nota50 = nota20 = nota10 = nota1 = 0
valor_sacar = int(input("Digite o valor que deseja sacar: R$"))
while True:
    if valor_sacar / 50 >= 1:
        nota50 += 1
        valor_sacar -= 50
    elif valor_sacar / 20 >= 1:
        nota20 += 1
        valor_sacar -= 20
    elif valor_sacar / 10 >= 1:
        nota10 += 1
        valor_sacar -= 10
    elif valor_sacar / 1 >= 1:
        nota1 += 1
        valor_sacar -= 1
    else:
        print(f"\nNotas a ser sacadas:")
        if nota50:
            print(f"Notas de R$50: {nota50}")
        if nota20:
            print(f"Notas de R$20: {nota20}")
        if nota10:
            print(f"Notas de R$10: {nota10}")
        if nota1:
            print(f"Notas do R$1 : {nota1}")
        if valor_sacar:
            print(f"O caixa não tem cédulas suficiente para sacar os R${valor_sacar} restantes.")
        print("Retire o dinheiro do caixa.")
        break
