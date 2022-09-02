"""
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
"""
distancia = int(input("Distância da viagem: "))
if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50
print(f"Para uma distância de {distancia}km, o valor da passagem é de R${preco:.2f}.")
