"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
while True:
    num = int(input("Digite um número inteiro qualquer: "))
    print("Deseja converter para qual base:\n"
          "[1] BINÁRIO\n"
          "[2] OCTAL\n"
          "[3] HEXADECIMAL")
    opc = int(input("Sua opção: "))

    if opc == 1:
        print(f"{num} em binário é {bin(num)[2:]}")
        break
    elif opc == 2:
        print(f"{num} em octal é {oct(num)[2:]}")
        break
    elif opc == 3:
        print(f"{num} em hexadecimal é {hex(num)[2:]}")
        break
    print("Opção inválida.\n\n")
