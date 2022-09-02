"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valore e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
resp = "S"
qtd = media = maior = menor = 0
while resp != "N":
    num = int(input("Digite um número inteiro: "))
    if qtd == 0:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    qtd += 1
    media += num
    resp = input("Deseja continuar [S/n] ").upper()
media /= qtd
print(f"Foram digitados {qtd} números\n"
      f"A média é de {media:.2f}\n"
      f"O maior valor digitado foi: {maior}\n"
      f"O menor valor digitado foi: {menor}")
