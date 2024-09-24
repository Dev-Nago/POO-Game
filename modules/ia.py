import time
import numpy as np

def ia(defendant,attacker):
    ############ IA ###########
        time.sleep(3)
        ia_choice = ["A","B","C","D"]
        if defendant.__class__.__name__ == "Wizard":
            choice = np.random.choice(ia_choice)
            if choice == "A":
                print("--- IA ---\n")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker)
            elif choice == "B":
                print("--- IA ---\n")
                defendant.blizzard(defendant,attacker)
                defendant.check_death(attacker)
            else:
                print("--- IA ---\n")
                defendant.boost_attack(defendant)
        if defendant.__class__.__name__ == "Warrior":
            choice = np.random.choice(ia_choice)
            if choice == "A":
                print("--- IA ---\n")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker)
            elif choice == "B":
                print("--- IA ---\n")
                defendant.whirlwind(defendant,attacker)
                defendant.check_death(attacker)
            else:
                print("--- IA ---\n")
                defendant.boost_attack(defendant)
        if defendant.__class__.__name__ == "Archer":
            choice = np.random.choice(ia_choice)
            if choice == "A":
                print("--- IA ---\n")
                defendant.normal_attack(defendant,attacker)
                defendant.check_death(attacker)
            elif choice == "B":
                print("--- IA ---\n")
                defendant.salve(defendant,attacker)
                defendant.check_death(attacker)
            elif choice == "D":
             defendant.healthPotion(defendant)
            else:
                print("--- IA ---\n")
                defendant.boost_attack(defendant)
        time.sleep(3)
        ##########################