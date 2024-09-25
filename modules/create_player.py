import numpy as np
from modules.Character import *
from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *
import sys
from app import game

def create_player(nom_attacker,classe):
    if classe == "A":
        attacker = Wizard(nom_attacker)
    elif classe == "B":
        attacker = Warrior(nom_attacker)
    elif classe == "C":
        attacker = Archer(nom_attacker)        
    else:
        print("!!!! Cette classe n'existe pas.... !!!! Seulement (A,B,C), Exit...\n")
        sys.exit()
    return attacker
