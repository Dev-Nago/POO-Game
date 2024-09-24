from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *
from modules.Character import *
from modules.player import *
from modules.ia import *
from modules.create_player import *
from modules.create_ia import *
import sys
import numpy as np
import time

def game():

    nom_attacker = input("Quel est votre Nom ?\n")
    time.sleep(1)
    nom_defendant = input("Quel est le nom de votre Rival ?\n")
    time.sleep(1)
    classe = input("Choisir votre classe : A = Magicien, B = Guerrier, C = Archer\n")
    time.sleep(1)
    attacker = create_player(nom_attacker,classe)
    defendant = create_ia(nom_defendant)

    while attacker.check_death(defendant) or defendant.check_death(attacker):
            player(attacker,defendant)
            ia(defendant,attacker)
        
game()