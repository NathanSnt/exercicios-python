"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação.
Depois mostre:
- Apenas os 5 primeiros colocados.
- Os últimos 4 colocados da tabela.
- Uma lista com os times em ordem alfabética.
- Em que posição na tabela está o time do chapecoense. (chapecoense não está na tabela, então usarei o Santos.)
"""
tabela = ("América-MG", "Athletico-PR", "Atlético-GO", "Atlético-MG", "Avaí", "Botafogo", "Ceará SC",
          "Corinthians", "Coritiba", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Internacional",
          "Juventude", "Palmeiras", "Bragantino", "Santos", "São Paulo")

print(f"O cinco primeiros colocados na tabela: ", end='')
for x in range(0, 5):
    print(tabela[x], end=', ' if x != 4 else '.')

print("\nOs 4 últimos da tabela: ", end='')
for x in range(-4, 0):
    print(tabela[x], end=', ' if x != -1 else '.')

print("\nTabela em ordem alfabética: ", end='')
alfabetico = sorted(tabela)
print(alfabetico)

print(f"O Santos está na {tabela.index('Santos')+1}º posição.")
