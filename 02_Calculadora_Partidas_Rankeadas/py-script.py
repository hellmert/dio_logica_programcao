"""
Resolução do Desafio proposto, utilizando Python
"""

def rankingVitorias(v, d, saldoVitorias):
    ranking = {10: 'Ferro', 20: 'Bronze', 50:'Prata', 80: 'Ouro', 90: 'Diamante', 100: 'Lendário', 1000000: 'Imortal'}

    for k in ranking:
        if saldoVitorias(v, d) <= k:
            ranking = ranking[k]
            break
    print(f'O herói tem saldo de {saldoVitorias(v, d)} e está no nível {ranking}.')


def saldoVitorias(v:int, d:int) -> int:
    return v - d


def main() -> str:
    v = int(input('N° de Vitórias: '))
    d = int(input('N° de Derrotas: '))
    return rankingVitorias(v, d, saldoVitorias)

main()