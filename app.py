from modules.Character import *
from modules.Wizard import *
from modules.Warrior import *
from modules.Archer import *

magicien = Wizard("Merlin")
guerrier = Warrior("Lancelot")
archer = Archer("Legolas")
guerrier.showHP(guerrier)
magicien.showHP(magicien)
magicien.attack_launch(magicien,guerrier)
guerrier.showHP(guerrier)
guerrier.attack_launch(magicien,guerrier)
magicien.showHP(magicien)
magicien.healthPotion(magicien)
magicien.attack_launch(magicien,guerrier)
magicien.attack_launch(magicien,guerrier)
magicien.attack_launch(magicien,guerrier)
magicien.attack_launch(magicien,guerrier)
magicien.attack_launch(magicien,guerrier)
getattr(guerrier,"hp")
getattr(magicien,"potion")
magicien.healthPotion(magicien)
magicien.healthPotion(magicien)
magicien.healthPotion(magicien)
getattr(magicien,"potion")