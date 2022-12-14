
import random
from weapon import Weapon

class Robot:
    def __init__(self, name):

        self.name = name
        self.health = 200
        self.active_weapon = Weapon("Sword", 30)
        self.kick_debuff = 0


    def attack(self, dinosaur):
        weapon_choice = input(f"Choose {self.name}'s weapon. Type 'Sword', 'Gun', or 'Kick'. ")
        if weapon_choice == "Sword":
            self.active_weapon = Weapon("Sword", 30) #Standard weapon with same damage as dino
        elif weapon_choice == "Gun":
            self.active_weapon = Weapon("Gun", 25) #Weaker weapon, but reduces "accuracy" of dino by 20%
        elif weapon_choice == "Kick":
            self.active_weapon = Weapon("Kick", 10) #Weakest weapon, but adds damage each round of use and reduces dino's accuracy by 10%
        else:
            pass

        attack_result = random.randint(1,100)
        if attack_result <= 5:
            print(f"{self.name} attacks but misses {dinosaur.name}!")
        elif attack_result >= 96:
            dinosaur.health -= self.active_weapon.attack_power*1.5+self.kick_debuff
            print(f"{self.name} attacks and scores a CRITICAL HIT! {dinosaur.name} takes {self.active_weapon.attack_power*1.5+self.kick_debuff} damage!")
        else:
            dinosaur.health -= self.active_weapon.attack_power+self.kick_debuff
            print(f"{self.name} attacks! {dinosaur.name} takes {self.active_weapon.attack_power+self.kick_debuff} damage!")
        
        if self.active_weapon.name == "Kick":
            self.kick_debuff += 10