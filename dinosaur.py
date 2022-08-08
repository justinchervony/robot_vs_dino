


import random


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 200
        self.crit_buff = 0
        self.turns_since_crit = 0


    def attack(self, robot):
        attack_result = random.randint(1,100)
        attack_result += self.crit_buff
        if self.turns_since_crit < 3: #prevents spamming of abilities to negate crits for the whole fight
            if robot.active_weapon.name == "Gun":
                attack_result -= 20
            elif robot.active_weapon.name == "Kick":
                attack_result -= 10
        else:
            pass

        if attack_result <= 5:
            print(f"{self.name} attacks but misses {robot.name}!")
            self.turns_since_crit += 1
        elif attack_result >= 81: #dino has higher crit chance
            robot.health -= self.attack_power*1.5
            self.crit_buff += 20 #if dino crits, they boost their crit chance significantly
            print(f"{self.name} attacks and scores a CRITICAL HIT! {robot.name} takes {self.attack_power*1.5} damage!")
            self.turns_since_crit = 0
        else:
            robot.health -= self.attack_power
            print(f"{self.name} attacks! {robot.name} takes {self.attack_power} damage!")
            self.turns_since_crit += 1
