#! /usr/bin/env python
import random, sys, time
import pygame as pg
import fighter
import name_generator as ng


class Battle:
    def __init__(
        self,
        fighter1: fighter.Fighter,
        fighter2: fighter.Fighter,
        time_betw_round: float = 0.1,
    ):
        self.ftr1 = fighter1
        self.ftr2 = fighter2
        self.over = False
        self.round_wait = time_betw_round

    def run(self, screen: pg.Surface, clock):
        leftside = self.ftr1
        rightside = self.ftr2
        leftside.rect.left, leftside.rect.top = (200, 300)
        rightside.rect.left, leftside.rect.top = (600, 300)
        pg.draw.circle(
            screen, leftside.color, leftside.rect.center, leftside.rect.width / 2
        )
        pg.draw.circle(
            screen, rightside.color, rightside.rect.center, rightside.rect.width / 2
        )
        if self.ftr1.timer < self.ftr2.timer:
            self.ftr1.whack(self.ftr2, False)
            self.ftr2.timer -= self.ftr1.timer
            self.ftr1.timer = self.ftr1.speed
        elif self.ftr2.timer < self.ftr1.timer:
            self.ftr2.whack(self.ftr1, False)
            self.ftr1.timer -= self.ftr2.timer
            self.ftr2.timer = self.ftr2.speed
        else:
            self.print_timer()
            self.ftr2.whack(self.ftr1, True)
            self.ftr1.timer = self.ftr1.speed
            self.ftr2.timer = self.ftr2.speed

        if self.ftr1.health < 0:
            self.ftr2.wins += 1
            print(
                f"{self.ftr2.name} wins the fight with {self.ftr2.health} health left ({self.ftr2.wins}total wins)"
            )
            self.over = True
        elif self.ftr2.health < 0:
            self.ftr1.wins += 1
            print(
                f"{self.ftr1.name} wins the fight with {self.ftr1.health} health left ({self.ftr1.wins}total wins)"
            )

            self.over = True
        time.sleep(self.round_wait)

    def print_timer(self):
        print(
            f"{self.ftr1.name}'s timer is {self.ftr1.timer}, {self.ftr2.name}'s timer is {self.ftr2.timer}"
        )

    def initialize(resolution):
        # pygame.init() will initialize all
        # imported module
        pg.init()
        if not pg.font:
            print("warning: font failed to start up")
        # initialize window and settings
        screen = pg.display.set_mode(resolution)
        pg.display.set_caption("Hunter of the Green Pack")
        # init clock for timers
        clock = pg.time.Clock()
        # basic font for console and buttons
        base_font = pg.font.Font(None, 32)
        return screen, clock, base_font


def main():
    res = [800, 400]
    screen, clock, console_font = Battle.initialize(res)
    background = pg.image.load("../images/battle_background_forest.png").convert_alpha()

    hercules = fighter.Fighter("Herc", 100, 28, 15, 100)
    random_fighter = fighter.Fighter("Rando McDumb")
    hercules.print()
    random_fighter.print()
    fight_club = Battle(hercules, random_fighter, 0.5)

    while True:
        for event in pg.event.get():

            # if user types QUIT then the screen will close
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((100, 200, 200))
        screen.blit(background, screen.get_rect())

        if fight_club.over:
            print("over")
            if fight_club.ftr1.health < 0:
                winner = fight_club.ftr1
            else:
                winner = fight_club.ftr2
            winner.health = winner.maxhealth
            new_random_fighter = fighter.Fighter()
            winner.print()
            new_random_fighter.print()
            fight_club = Battle(winner, new_random_fighter, 0.5)
        else:
            fight_club.run(screen, clock)

        pg.display.update()


# Execute Game
if __name__ == "__main__":
    args = sys.argv[1:]
    main()
