"""
Resolução do desafio em minha lingaguem principal, Python.
"""

# Requisição de dados
nome = input('Qual seu nome, herói? ')
xp = int(input(f'Quero te ajudar, {nome}, porém preciso saber seu nível de experiência. Qual seu xp atual? '))

# Array
level = {1000: 'Ferro', 2000: 'Bronze', 5000: 'Prata', 7000: 'Ouro', 8000: 'Platina', 9000: 'Ascendente', 10000: 'Imortal', 1000000: 'Radiante'}

# Condição Lógica
for k in level:
    if xp <= k:
        xp = level[k]
        break

# Output
print(f'Muito bom, herói {nome}, você está no nível {xp}. Vamos trabalhar para melhorar isso?')