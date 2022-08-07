import random
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot_combatant = Robot("Mechazord")
        self.dino_combatant = Dinosaur("Rex", 35)
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    def display_welcome(self):
        print("Welcome to the game!")
    def battle_phase(self):
        combatant_start = random(1)
        while self.robot_combatant.health < 0 and self.dino_combatant.health < 0:
            if combatant_start % 2 == 0:
                self.robot_combatant.attack()
            else:
                self.dino_combatant.attack()
    def display_winner(self):
        if self.robot_combatant <= 0:
            print(f"The winner is {self.dino_combatant.name}!")
        else:
            print(f"The winner is {self.robot_combatant.name}!")
        pass