


import random


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    def attack(self, robot):
        attack_result = random.randint(1,100)
        if attack_result <= 5:
            print(f"{self.name} attacks but misses {robot.name}!")
        elif attack_result >= 96:
            robot.health -= self.attack_power*1.5
            print(f"{self.name} attacks and scores a CRITICAL HIT! {robot.name} takes {self.attack_power*1.5} damage!")
        else:
            robot.health -= self.attack_power
            print(f"{self.name} attacks! {robot.name} takes {self.attack_power} damage!")
