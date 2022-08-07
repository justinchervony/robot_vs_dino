from weapon import Weapon

class Robot:
    def __init__(self, name):

        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Laser Sword", 30)
        pass
    def attack(self, dinosaur):
        dinosaur.health -= self.attack_power
        print(f"{self.name} attacks! {dinosaur.name} takes {self.active_weapon.attack_power} damage!")