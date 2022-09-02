"""
Crie um programa onde o usuário digite um expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
expr = input("Digite um expressão qualquer: ")

parenteses = 0
for x in expr:
    if x == "(":
        parenteses += 1
    elif x == ")":
        parenteses -= 1

if parenteses == 0:
    print("A sua expressão está correta.")
else:
    print("A sua expressão está incorreta.")
