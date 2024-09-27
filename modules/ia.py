import time
import numpy as np

def ia(defendant,attacker):
    ############ IA ###########
        time.sleep(3)
        ia_choice = ["A","B","C","D"]
        choice = np.random.choice(ia_choice)
                #Fonctions de l'IA Wizard
        if defendant.__class__.__name__ == "Wizard":
            if choice == "A":
                print("--- IA ---")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker,defendant)
            elif choice == "B":
                print("--- IA ---")
                defendant.blizzard(defendant,attacker)
                defendant.check_death(attacker,defendant)
            elif choice == "C":
                print("--- IA ---")
                defendant.boost_attack(defendant)
            else:
                print("--- IA ---")
                defendant.healthPotion(defendant)
                #Fonctions de l'IA Warrior
        if defendant.__class__.__name__ == "Warrior":
            if choice == "A":
                print("--- IA ---")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker,defendant)
            elif choice == "B":
                print("--- IA ---")
                defendant.whirlwind(defendant,attacker)
                defendant.check_death(attacker,defendant)
            elif choice == "C":
                print("--- IA ---")
                defendant.boost_attack(defendant)
            else:
                print("--- IA ---")
                defendant.healthPotion(defendant)
                # Fonctions de l'IA Archer
        if defendant.__class__.__name__ == "Archer":
            if choice == "A":
                print("--- IA ---")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker,defendant)
            elif choice == "B":
                print("--- IA ---")
                defendant.salve(defendant,attacker)
                defendant.check_death(attacker,defendant)
            elif choice == "C":
                print("--- IA ---")
                defendant.boost_attack(defendant)
            else:
                print("--- IA ---")
                defendant.healthPotion(defendant)
        time.sleep(3)
        ##########################