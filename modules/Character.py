import sys

class Character:
    def __init__(self,name):
        self.name = name
        self.potion = 3


    def check_death(self,defendant,attacker):
        if getattr(defendant,"hp") < 1:
            print("==========================================================================")
            print("             Le personnage ",defendant.name,"(",defendant.type,")"," est mort.")
            print("         *** ",attacker.name,"(",attacker.type,")"," est le grand vainqueur ! ***")
            print("                     Partie Terminée. Exit...")
            print("==========================================================================")
            sys.exit()
            return False
        else:
            return True

    def showHP(self,character):
        print("* ",character.name," a ",character.hp," HP. *\n")
        
    def normal_attack(self,attacker,defendant):
        damage = defendant.defense * attacker.attack / 50
        actual_hp = defendant.hp - damage
        setattr(defendant,"hp",actual_hp)
        print("***",attacker.name," lance une attaque sur ",defendant.name,"***")
        print("*",defendant.name," a perdu ",damage," à la suite d'une attaque de ",attacker.name,"*")
        print(" -- ",defendant.name," a ",defendant.hp," HP restant. ---\n")

    def healthPotion(self,character):
        if character.potion > 0:
            actual_hp = character.hp + 200
            actual_potion = character.potion - 1
            setattr(character,"hp",actual_hp)
            setattr(character,"potion",actual_potion)
            print("* ",character.name," a regenerer 200HP, HP actuel : ",actual_hp," *\n")
        else:
            print("* ",character.name," n'a plus de potion disponible. *\n")

    def boost_attack(self, character):
        if character.hp > 200:
            boost_attack = character.attack + 10
            setattr(character, "attack", boost_attack)
            losthp = character.hp - 50
            setattr(character,"hp",losthp)
            print("* ",character.name," sacrifie 50HP. Total HP : ",character.hp," *")
            print("* ",character.name," vient de booster son attaque, attaque total : ",boost_attack," *\n")
        else:
            print("* ",character.name," ne peut pas booster son attaque \n"," HP actuel : ",character.hp,", ",200 - character.hp,"HP sont necessaire pour le boost. *\n")