"""
Faça um programa que leia o sexo de uma pessoa, mas só aceito os valores 'M' ou 'F'.
Caso esteja errdo, peça a digitação novamente até ter um valor correto.
"""
sexo = ""
while sexo != 'F' and sexo != 'M':
    sexo = input("Digite o seu sexo [M/F]: ").upper()
    if sexo != 'F' and sexo != 'M':
        print("Opção inválida!")
print(f"Seu sexo é: {'Masculino' if sexo == 'M' else 'Feminino'}")
