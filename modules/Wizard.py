from modules.Character import *
class Wizard(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp = 250
        self.defense = 50
        self.attack = 50