import time
import numpy as np
from modules.Character import *
from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *

def create_ia(nom_defendant):
    liste = ["Magicien","Guerrier","Archer"]
    rivals = np.random.choice(liste)

    if rivals == "Magicien":
        defendant = Wizard(nom_defendant)
    elif rivals == "Warrior":
        defendant = Warrior(nom_defendant)
    else:
        defendant = Archer(nom_defendant)
    return defendant