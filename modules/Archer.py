from modules.Character import *
class Archer(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp = 400
        self.defense = 70
        self.attack = 40