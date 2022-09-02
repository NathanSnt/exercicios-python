"""
Escreva um programa que leia uma temperatura digitada em ºC e converta para ºF.
"""
celsius = float(input("Digite uma temperatura em celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius:.1f}ºC igual a {fahrenheit:.1f}ºF")
