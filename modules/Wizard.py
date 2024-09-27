from modules.Character import Character

class Wizard(Character):
    def __init__(self, name,type) -> None:
        super().__init__(name)
        self.hp = 250
        self.defense = 50
        self.attack = 70
        self.special_attack = 8
        self.type = type

    def blizzard(self,attacker,defendant):
        if attacker.special_attack > 0:   
            damage = round(defendant.defense * attacker.attack / 30)
            actual_hp = round(defendant.hp - damage)
            setattr(defendant,"hp",actual_hp)
            attacker.special_attack -= 1
            print("***",attacker.name," lance un * Blizzard * sur ",defendant.name,"***")
            print("*",defendant.name," a perdu ",damage," à la suite du Blizzard de ",attacker.name,"*")
            print(" -- ",defendant.name," a ",defendant.hp," HP restant. ---\n")
        else:
            print("* ",attacker.name," n'a plus d'attaque spéciale... *\n")