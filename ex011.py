"""
Faça um programa que leia a altura e a largura de uma parede em metros. Calcule a sua área e a quantidade de tinta
necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""
altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

area = altura * largura

print(f"A parede tem {area:.2f}m²")
tinta = area / 2

print(f"Voce precisará de {tinta:.1f} litros de tinta para conseguir pintar toda a parede.")
