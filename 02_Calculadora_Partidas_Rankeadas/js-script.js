//// Resolução do desafio em linguagem trabalhada em aula, JavaScript.

rankingVitorias(200, 100)

function rankingVitorias(v, d){
    let saldo = v - d
    let ranking = {10: 'Ferro', 20: 'Bronze', 50:'Prata', 80: 'Ouro', 90: 'Diamante', 100: 'Lendário', 1000000: 'Imortal'}

    for (k in ranking){
    if (saldo <= k){
        ranking = ranking[k]
        break
        }
    }
    console.log(`O herói tem saldo de ${saldo} e está no nível ${ranking}.`)
}
