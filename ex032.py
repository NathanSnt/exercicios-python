"""
Faça um programa queleia um ano qualquer e mostre se ele é bissexto.
"""
ano = int(input("Digite um ano qualquer: "))
if ano % 4 == 0:
    if ano % 100 != 0:
        print(f"O ano {ano} é BISSEXTO.")
    elif ano % 400 == 0:
        print(f"O ano {ano} é BISSEXTO.")
    else:
        print(f"O ano {ano} não é BISSEXTO.")
else:
    print(f"O ano {ano} não é BISSEXTO.")
