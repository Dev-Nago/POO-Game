import time
import numpy as np
from modules.Character import *
from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *

def player(attacker,defendant):
      ######### JOUEUR ##########
        print("Action...")
        attaque = input("A = Attaque normal, B = Attaque Spéciale, C = Boost Attaque, D = Potion(200HP)\n")
        time.sleep(1)
        if attaque == "A":
            print("--- JOUEUR ---")
            attacker.normal_attack(attacker,defendant)
            attacker.check_death(defendant,attacker)
        elif attaque == "B":
            if attacker.__class__.__name__ == "Wizard":
                print("--- JOUEUR ---")
                attacker.blizzard(attacker,defendant)
                attacker.check_death(defendant,attacker)
            if attacker.__class__.__name__ == "Warrior":
                print("--- JOUEUR ---")
                attacker.whirlwind(attacker,defendant)
                attacker.check_death(defendant,attacker)           
            if attacker.__class__.__name__ == "Archer":
                print("--- JOUEUR ---")
                attacker.salve(attacker,defendant)
                attacker.check_death(defendant,attacker)
        elif attaque == "C":
            print("--- JOUEUR ---")
            attacker.boost_attack(attacker)
        elif attaque == "D":
             print("--- JOUEUR ---")
             attacker.healthPotion(attacker)
        else:
            print("Mauvaise Lettre, A,B,C,D uniquement.\n")
        ######### JOUEUR #########