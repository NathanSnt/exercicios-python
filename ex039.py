"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import datetime
ANO = datetime.now().year
nasc = int(input("Digite o ano do seu nascimento: "))

idade = ANO - nasc
if idade < 18:
    print(f"Ainda não está na hora de você se alistar\n"
          f"Falta {18-idade} anos para você ter que se alistar.")
elif idade == 18:
    print(f"Você já está na idade de se alistar no serviço militar.\n"
          f"Compareça ao posto mais próximo da sua casa.")
else:
    print(f"Você ja passou da hora de se alistar no seviço militar.\n"
          f"Voce deveria ter se alistado a {idade-18} anos atrás.")
