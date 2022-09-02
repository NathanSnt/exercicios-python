"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso ideal
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Com IMC de { imc:.1f} você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Com IMC de {imc:.1f} você está no peso ideal.")
elif 25 <= imc < 30:
    print(f"Com IMC de {imc:.1f} você está com sobrepeso.")
elif 30 <= imc < 40:
    print(f"Com IMC de {imc:.1f} você está com obesidade.")
else:
    print(f"Com IMC de {imc:.1f} você está com obesidade mórbida.")
