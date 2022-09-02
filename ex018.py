"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan
angulo = float(input("Digite um angulo qualquer: "))

print(f"cosseno: {cos(angulo):.2f}\nseno: {sin(angulo):.2f}\ntangente: {tan(angulo):.2f}")
