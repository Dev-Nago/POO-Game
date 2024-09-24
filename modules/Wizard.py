from modules.Character import Character

class Wizard(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp = 250
        self.defense = 50
        self.attack = 50
    def blizzard(self,attacker,defendant):
        damage = defendant.defense - attacker.attack / 4
        actual_hp = defendant.hp - damage
        setattr(defendant,"hp",actual_hp)
        print("***",attacker.name," lance un Blizzard sur ",defendant.name,"***")
        print("*",defendant.name," a perdu ",damage," à la suite du Blizzard de ",attacker.name,"*")
        print(" -- ",defendant.name," a ",defendant.hp," points de vie restant. ---\n")