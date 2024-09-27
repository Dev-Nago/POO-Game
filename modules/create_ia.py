import numpy as np
from modules.Character import *
from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *

def create_ia():
    nom_defendant = input("Quel est le nom de votre Rival ?\n")
    time.sleep(2)
    liste = ["Magicien","Guerrier","Archer"]
    rivals = np.random.choice(liste)

    if rivals == "Magicien":
        defendant = Wizard(nom_defendant,"IA")
    elif rivals == "Warrior":
        defendant = Warrior(nom_defendant,"IA")
    else:
        defendant = Archer(nom_defendant,'IA')
    return defendant