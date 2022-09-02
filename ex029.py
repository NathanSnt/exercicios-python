"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
"""
velocidade = int(input("Digite a velocidade do carro: "))

LIMITE = 80

if velocidade > LIMITE:
    print("VEICULO MULTADO!")
    multa = (velocidade - LIMITE) * 7
    print(f"Valor da multa: R${multa:.2f}")
else:
    print("Tudo normal.")
