#! /usr/bin/env python
import random, sys, time

class Fighter:
    def __init__(self, name: str, health=False, attack=False, defense=False, speed=False):
        self.name = name
        self.health = health if health else random.randint(100, 120)
        self.attack = attack if attack else random.randint(20, 30)
        self.defense = defense if defense else random.randint(10, 20)
        self.speed = speed if speed else random.randint(60, 100)
        self.timer = self.speed

    def whack(self, target):
        if self.attack > target.defense:
            target.health -= (self.attack - target.defense)
            target.timer -= self.timer
            self.timer = self.speed

    def print(self):
        print('name: ' + self.name + ', health: ' + str(self.health) + ', attack: ' + str(self.attack) + ', defense: ' + str(self.defense) + ', speed: ' + str(self.speed))

class Battle:
    def __init__(self, fighter1: Fighter, fighter2: Fighter, time_betw_rounds: float=0.1):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.time_betw_rounds = time_betw_rounds

    def run(self):
        while self.fighter1.health > 0 and self.fighter2.health > 0:
            if self.fighter1.timer == 0:
                # print(f'{self.fighter1.name} attacks {self.fighter2.name}, {self.fighter2.name} has {self.fighter2.health} health left')
                # self.print_timer()
                self.fighter1.whack(self.fighter2)
            elif self.fighter2.timer == 0:
                # print(f'{self.fighter2.name} attacks {self.fighter1.name}, {self.fighter1.name} has {self.fighter1.health} health left')
                # self.print_timer()
                self.fighter2.whack(self.fighter1)
            else:
                self.print_timer()
                if self.fighter1.timer > self.fighter2.timer:
                    self.fighter1.timer -= self.fighter2.timer
                    self.fighter2.timer = 0
                else:
                    self.fighter1.timer -= self.fighter1.timer
                    self.fighter2.timer = 0
                self.print_timer()
                # print(f'a moment passes and the fighters gather strength')
                
            time.sleep(self.time_betw_rounds)

        if self.fighter1.health > 0:
            print(f'{self.fighter1.name} wins the fight with {self.fighter1.health} health left')
        else:
            print(f'{self.fighter2.name} wins the fight with {self.fighter2.health} health left')

    def print_timer(self):
        print(f"{self.fighter1.name}'s timer is {self.fighter1.timer}, {self.fighter2.name}'s timer is {self.fighter2.timer}")
                
def main():
    hercules = Fighter('Herc', 100, 28, 15, 100)
    random_fighter = Fighter('Rando McDumb')
    hercules.print()
    random_fighter.print()
    fight_club = Battle(hercules, random_fighter)
    fight_club.run()

# Execute Game
if __name__ == "__main__":
    args = sys.argv[1:]
    main()
