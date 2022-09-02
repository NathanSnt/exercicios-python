"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
- Quantas pessoas tem mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres tem menos de 20 anos.
"""
mais18 = homens = mulher_menos_20 = qtd = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: [M/F]: ")[0].upper()
    if sexo not in "MF":
        print("Sexo inválido!")
    elif 0 > idade or idade > 120:
        print("Tem algo de errado com a idade...")
    else:
        if idade > 18:
            mais18 += 1
        if sexo == "M":
            homens += 1
        if sexo == "F" and idade < 20:
            mulher_menos_20 += 1
        qtd += 1
        continuar = input("Adicionar mais uma pessoa? [S/n]").upper()
        if continuar == "N":
            break
print(f"Foram lidos os dados de {qtd} {'pessoas' if qtd > 1 else 'pessoa'} sendo:\n"
      f"{mais18} {'pessoas' if mais18 > 1 else 'pessoa'} com mais de 18 anos.\n"
      f"{homens} {'pessoas' if homens > 1 else 'pessoa'} do sexo masculino.\n"
      f"{mulher_menos_20} {'mulheres' if mulher_menos_20 > 1 else 'mulher'} com mais de 20 anos.")
