"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugar e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
"""
CUSTO_KM = 0.15
CUSTO_DIA = 60

dias = int(input("Por quantos dias o carro ficou alugado? "))
km = float(input("Quantos km o carro percorreu? "))

valor_dias = dias * CUSTO_DIA
valor_km = km * CUSTO_KM
valor = valor_dias + valor_km

print(f"Você percorreu {km}km em {dias} dias com o carro, e deve pagar um total de R${valor:.2f} pelo aluguel do carro.")
print(f"Sendo R${valor_dias} pelos {dias} dias de aluguel", end=" ")
print(f"e R${valor_km} pelos {km}km percorridos.")
