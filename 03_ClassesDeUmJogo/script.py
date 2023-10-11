"""
Resolução do Desafio proposto, utilizando Python
"""

#Definição da Classe
class getHero(object):
    def __init__(self, name:str, age:int, category:str):
        self.name = name
        self.age = age
        self.category = category
        self.attackType = self._attackType()

    def _attackType(self) -> str:
        attack = {"mago": "magia",
                "guerreiro": "espada",
                "monge": "artes marciais",
                "ninja": "shuriken"}
        return attack[self.category]
    
    # Método Principal
    def attacking(self):
        print(f"{self.category.capitalize()} {self.name} atacou usando {self.attackType}")


# Instanciando os objetos
heroi00 = getHero("Koza", 47, "guerreiro")
heroi01 = getHero("Jin", 23, "monge")
heroi02 = getHero("Fuu", 89, "mago")
heroi03 = getHero("Mugen", 16, "ninja")

## Chamando o método princial
heroi00.attacking()
heroi01.attacking()
heroi02.attacking()
heroi03.attacking()       
