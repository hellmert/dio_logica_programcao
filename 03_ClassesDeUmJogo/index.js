//// Resolução do desafio em linguagem trabalhada em aula, JavaScript.

// Definição da classe

class getHero{
    constructor(name, age, category){
        this.name = name
        this.age = age
        this.category = category
        this.attackType = this.attackType()
    }

    attackType(){
        let attack = {"mago": "magia",
                    "guerreiro": "espada",
                    "monge": "artes marciais",
                    "ninja": "shuriken"}
        return attack[this.category]
    }

    // Método principal
    attacking(){
        console.log(`${this.category[0].toUpperCase() + this.category.substring(1)} ${this.name} atacou usando ${this.attackType}.`)
    }
}

// Instanciando os objetos

let heroi00 = new getHero("Revy", 47, "guerreiro")
let heroi01 = new getHero("Eda", 23, "monge")
let heroi02 = new getHero("Baba Yaga", 89, "mago")
let heroi03 = new getHero("Roberta", 16, "ninja")

// Chamando o método princial

heroi00.attacking()
heroi01.attacking()
heroi02.attacking()
heroi03.attacking()