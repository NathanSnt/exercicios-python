"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
vogais = ("a", "e", "i", "o", "u")
palavras = ("sol", "mar", "montanha", "escola", "transporte", "aeroporto", "navio", "canal",
            "programa", "carro", "satelite", "janela", "computador", "sistema", "garrafa",
            "teclado", "tomada", "avenida")

print(f"{'PALAVRAS':^12}|{'VOGAIS':^10}")
for palavra in palavras:
    print(f"{palavra:<12}|", end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print()
