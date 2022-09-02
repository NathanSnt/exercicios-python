"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
"""
num = int(input("Digite um número de 0 a 9999: "))
if -1 < num < 10000:
    if num > 999:
        print(f'Unidade: {str(num)[3]}')
        print(f'Dezena: {str(num)[2]}')
        print(f'Centena: {str(num)[1]}')
        print(f'Milhar: {str(num)[0]}')
    elif num > 99:
        print(f'Unidade: {str(num)[2]}')
        print(f'Dezena: {str(num)[1]}')
        print(f'Centena: {str(num)[0]}')
    elif num > 9:
        print(f'Unidade: {str(num)[1]}')
        print(f'Dezena: {str(num)[0]}')
    else:
        print(f'Unidade: {str(num)[0]}')

else:
    print("O número tem de ser entre 0 e 9999")
