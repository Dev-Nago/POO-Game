from modules.Character import Character

class Archer(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp = 400
        self.defense = 70
        self.attack = 40
        self.special_attack = 5
        
    def salve(self,attacker,defendant):
        if attacker.special_attack > 0:
            damage = defendant.defense - attacker.attack / 5
            actual_hp = defendant.hp - damage
            setattr(defendant,"hp",actual_hp)
            attacker.special_attack -= 1
            print("***",attacker.name," lance une Salve sur ",defendant.name,"***")
            print("*",defendant.name," a perdu ",damage," à la suite de la Salve de ",attacker.name,"*")
            print(" -- ",defendant.name," a ",defendant.hp," points de vie restant. ---\n")
        else:
            print("* ",attacker.name," n'a plus d'attaque spéciale... *\n")