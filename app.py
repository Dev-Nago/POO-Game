from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *
from modules.Character import *
from modules.player import *
from modules.ia import *
from modules.create_player import *
from modules.create_ia import *
import numpy as np
import time

def game(attacker,defendant):

    print("__ ",attacker.name," est un ",attacker.__class__.__name__," avec ",attacker.hp,"HP ",attacker.attack,"Attaque et ",attacker.defense,"Defense. __")
    print("__ ",defendant.name," est un ",defendant.__class__.__name__," avec ",defendant.hp,"HP ",defendant.attack,"Attaque et ",defendant.defense,"Defense. __\n")
    time.sleep(2)
    print("Que le combat commence...\n")
    time.sleep(2)

    while attacker.check_death(defendant,attacker) or defendant.check_death(attacker,defendant):
            player(attacker,defendant)
            ia(defendant,attacker)
        
if __name__ == "__main__":
    attacker = create_player()
    defendant = create_ia()
    game(attacker,defendant)