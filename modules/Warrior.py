from modules.Character import *
import time

class Warrior(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp = 500
        self.defense = 100
        self.attack = 25

    def whirlwind(self,attacker,defendant):
        total_damage = 0
        for i in range(1,4):
            damage = defendant.defense - attacker.attack / 2
            total_damage += damage
            actual_hp = defendant.hp - damage
            setattr(defendant,"hp",actual_hp)
            print("***",attacker.name," lance un Whirlwind (",i,"/ 3 ) sur ",defendant.name,"***")
            print("* ",defendant.name," perd ", damage, " points de vie par attaque ! *")
            print("*",defendant.name," a perdu au total ",total_damage," à la suite du Whirlwind de ",attacker.name,"*")
            print(" -- ",defendant.name," a ",defendant.hp," points de vie restant. ---\n")
            time.sleep(1)