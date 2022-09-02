"""
Crie um programa que leia dois valores e mostree  um menu na tela:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
opc = 0

while opc != 5:
    print('\n\n', "=-"*20)
    print(f"Valor 1 = {valor1}\nValor 2 = {valor2}")
    print("Qual operação deseja realizar: \n"
          "[1] SOMAR\n"
          "[2] MULTIPLICAR\n"
          "[3] MAIOR\n"
          "[4] NOVOS VALORES\n"
          "[5] SAIR DO PROGRAMA")
    opc = int(input(">>> "))
    if opc < 1 or opc > 5:
        print("Opção inválida!")
    elif opc == 1:
        print(f"A soma de {valor1} e {valor2} é igual a {valor2 + valor1}")
    elif opc == 2:
        print(f"{valor1} x {valor2} = {valor1 * valor2}")
    elif opc == 3:
        if valor1 > valor2:
            print(f"O primeiro valor digitado ({valor1}) é maior que o segundo valor digitado ({valor2})")
        elif valor2 > valor1:
            print(f"O segundo valor digitado ({valor2}) é maior que o primeiro valor digitado ({valor1})")
        else:
            print("O primeiro valor digitado é igual ao segundo valor digitado, não existe maior.")
    elif opc == 4:
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
    elif opc == 5:
        print("\nAté a próxima.\n")
    sleep(2.5)
