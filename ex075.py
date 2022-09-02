"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
- Quantas vezes apareceu o valor 9.
- Em que posíção foi digitado o primeiro valor 3.
- Quais foram os números pares.
"""
pares = ''
tupla = (int(input("Digite um número inteiro: ")), int(input("Digite mais um número inteiro: ")),
         int(input("Digite um número inteiro denovo: ")), int(input("Digite um número inteiro outra vez: ")))
for x in tupla:
    if x % 2 == 0:
        pares += str(x) + ' '

nove = tupla.count(9)
tres = tupla.index(3) + 1
print(f"O número 9 apareceu {nove} vezes.\n"
      f"O número 3 apareceu pela primeira vez na posição {tres}.\n"
      f"Esses foram os números pares da tupla: {pares}")
