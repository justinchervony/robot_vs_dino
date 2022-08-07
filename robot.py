
import random
from weapon import Weapon

class Robot:
    def __init__(self, name):

        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Laser Sword", 30)
        pass
    def attack(self, dinosaur):
        attack_result = random.randint(1,100)
        if attack_result <= 5:
            print(f"{self.name} attacks but misses {dinosaur.name}!")
        elif attack_result >= 96:
            dinosaur.health -= self.active_weapon.attack_power*1.5
            print(f"{self.name} attacks and scores a CRITICAL HIT! {dinosaur.name} takes {self.active_weapon.attack_power*1.5} damage!")
        else:
            dinosaur.health -= self.active_weapon.attack_power
            print(f"{self.name} attacks! {dinosaur.name} takes {self.active_weapon.attack_power} damage!")