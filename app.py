from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *
from modules.Character import *
import numpy as np
import time

def game():
    nom_attacker = input("Quel est votre nom ?\n")
    time.sleep(1)
    nom_defendant = input("Quel est le nom de votre Rival ?\n")
    time.sleep(1)
    classe = input("Choisir votre classe : A = Magicien, B = Guerrier, C = Archer\n")
    time.sleep(1)

    if classe == "A":
        attacker = Wizard(nom_attacker)
    elif classe == "B":
        attacker = Warrior(nom_attacker)
    elif classe == "C":
        attacker = Archer(nom_attacker)
    else:
        print("Mauvaise Lettre rentrée, veuillez choisir entre A B ou C")
    liste = ["Magicien","Guerrier","Archer"]
    rivals = np.random.choice(liste)

    if rivals == "Magicien":
        defendant = Wizard(nom_defendant)
    elif rivals == "Warrior":
        defendant = Warrior(nom_defendant)
    else:
        defendant = Archer(nom_defendant)

    while attacker.check_death(defendant):

        print("Choisir votre attaque...\n")
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
        
        ############ IA ###########
        time.sleep(3)
        ia_choice = ["A","B"]
        if defendant.__class__.__name__ == "Wizard":
            choice = np.random.choice(ia_choice)
            if choice == "A":
                print("--- IA ---\n")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker)
            else:
                print("--- IA ---\n")
                defendant.blizzard(defendant,attacker)
                defendant.check_death(attacker)
        if defendant.__class__.__name__ == "Warrior":
            choice = np.random.choice(ia_choice)
            if choice == "A":
                print("--- IA ---\n")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker)
            else:
                print("--- IA ---\n")
                defendant.whirlwind(defendant,attacker)
                defendant.check_death(attacker)
        if defendant.__class__.__name__ == "Archer":
            choice = np.random.choice(ia_choice)
            if choice == "A":
                print("--- IA ---\n")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker)
            else:
                print("--- IA ---\n")
                defendant.salve(defendant,attacker)
                defendant.check_death(attacker)
        time.sleep(3)
        ##########################
game()