// Resolução do desafio em linguagem trabalhada em aula, JavaScript.


// Dados
let nome = "Ana";
let level = {1000: 'Ferro', 2000: 'Bronze', 5000: 'Prata', 7000: 'Ouro', 8000: 'Platina', 9000: 'Ascendente', 10000: 'Imortal', 1000000: 'Radiante'};
let xp = 7856

// Condição Lógica
for (k in level){
    if (xp <= k){
        xp = level[k]
        break
    }
}

// Output
console.log(`O herói de nome ${nome} está no nível ${xp}.`);