import numpy as np
from modules.Character import *
from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *
import sys
from app import game

def create_player():
    nom_attacker = input("Quel est votre Nom ?\n")
    time.sleep(1)
    classe = input("Choisir votre classe : A = Magicien, B = Guerrier, C = Archer\n")
    time.sleep(1)
    if classe == "A":
        attacker = Wizard(nom_attacker,"JOUEUR")
    elif classe == "B":
        attacker = Warrior(nom_attacker,"JOUEUR")
    elif classe == "C":
        attacker = Archer(nom_attacker,"JOUEUR")
    else : 
        print("!!!! Cette classe n'existe pas.... !!!! Seulement (A,B,C), Exit...\n")
        sys.exit()
    return attacker