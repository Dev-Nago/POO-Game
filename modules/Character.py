class Character:
    def __init__(self,name) -> None:
        self.name = name
        self.potion = 3

    def showHP(self,character):
        print(character.name," a ",character.hp," points de vie.")
        
    def attack_launch(self,attacker,defendant):
        damage = defendant.defense - attacker.attack / 2
        actual_hp = defendant.hp - damage
        setattr(defendant,"hp",actual_hp)
        print("***",attacker.name," lance une attaque sur ",defendant.name,"***")
        print("*",defendant.name," a perdu ",damage," à la suite d'une attaque de ",attacker.name,"*")
        if getattr(defendant,"hp") < 1:
            print("Le personnage ",defendant.name," est mort.")

    def healthPotion(self,character):
        if character.potion > 0:
            actual_hp = character.hp + 100
            actual_potion = character.potion - 1
            setattr(character,"hp",actual_hp)
            setattr(character,"potion",actual_potion)
            print(character.name," a regenerer ",100," HP, points de vie actuels : ",actual_hp)
        else:
            print(character.name," n'a plus de potion disponible.")