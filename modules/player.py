import time
import numpy as np
from modules.Character import *
from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *

def player(attacker,defendant):
      ######### JOUEUR ##########
        print("Choisir votre attaque...")
        attaque = input("A = Attaque normal, B = Attaque Spéciale\n")
        time.sleep(1)
        if attaque == "A":
            print("--- JOUEUR ---\n")
            attacker.normal_attack(attacker,defendant)
            attacker.check_death(defendant)
        elif attaque == "B":
            if attacker.__class__.__name__ == "Wizard":
                print("--- JOUEUR ---\n")
                attacker.blizzard(attacker,defendant)
                attacker.check_death(defendant)
            if attacker.__class__.__name__ == "Warrior":
                print("--- JOUEUR ---\n")
                attacker.whirlwind(attacker,defendant)
                attacker.check_death(defendant)           
            if attacker.__class__.__name__ == "Archer":
                print("--- JOUEUR ---\n")
                attacker.salve(attacker,defendant)
                attacker.check_death(defendant)
        else:
            print("Mauvaise Lettre, A ou B seulelment.\n")
        ######### JOUEUR #########