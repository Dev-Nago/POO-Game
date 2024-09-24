from modules.Character import *
class Warrior(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp = 500
        self.defense = 100
        self.attack = 25 