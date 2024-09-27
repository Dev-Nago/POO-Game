from modules.Character import *
import time

class Warrior(Character):
    def __init__(self, name,type) -> None:
        super().__init__(name)
        self.hp = 500
        self.defense = 120
        self.attack = 25
        self.special_attack = 3
        self.type = type

    def whirlwind(self,attacker,defendant):
        if attacker.special_attack > 0:
            total_damage = 0
            for i in range(1,4):
                damage = round(defendant.defense * attacker.attack / 50)
                total_damage += damage
                actual_hp = round(defendant.hp - damage)
                setattr(defendant,"hp",actual_hp)
                print("***",attacker.name," lance un * Whirlwind * (",i,"/ 3 ) sur ",defendant.name,"***")
                print("* ",defendant.name," perd ", damage, " HP par attaque ! *")
                print("*",defendant.name," a perdu au total ",total_damage," à la suite du Whirlwind de ",attacker.name,"*")
                print(" -- ",defendant.name," a ",defendant.hp," HP restant. ---\n")
                time.sleep(1)
            attacker.special_attack -= 1    
        else:
            print("* ",attacker.name," n'a plus d'attaque spéciale... *\n")