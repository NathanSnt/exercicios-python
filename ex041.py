"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import datetime
ANO = datetime.now().year

nasc = int(input("Digite o ano de nascimento do atleta: "))
idade = ANO - nasc

if idade <= 9:
    print(f"Com {idade} anos, o atleta se encaixa na categoria MIRIM")
elif idade <= 14:
    print(f"Com {idade} anos, o atleta se encaixa na categoria INFANTIL")
elif idade <= 19:
    print(f"Com {idade} anos, o atleta se encaixa na categoria JUNIOR")
elif idade <= 25:
    print(f"Com {idade} anos, o atleta se encaixa na categoria SÊNIOR")
else:
    print(f"Com {idade} anos, o atleta se encaixa na categoria MASTER")
