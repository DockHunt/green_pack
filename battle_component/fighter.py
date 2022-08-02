#! /usr/bin/env python
import random, sys, time
import pygame as pg
import name_generator as ng


class Fighter:
    def __init__(
        self,
        name: str = ng.get_name(),
        health=False,
        attack=False,
        defense=False,
        speed=False,
    ):
        self.name = name
        self.maxhealth = health if health else random.randint(100, 120)
        self.health = self.maxhealth
        self.attack = attack if attack else random.randint(20, 30)
        self.defense = defense if defense else random.randint(10, 20)
        self.speed = speed if speed else random.randint(60, 100)
        self.timer = self.speed
        self.wins = 0
        # rendering components
        self.surface = pg.Surface([50, 50])
        self.color = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ]

    def randomize_look():
        # WORK STARTS HERE
        pg.draw.circle(
            screen, leftside.color, leftside.rect.center, leftside.rect.width / 2
        )
        # AND HERE

    def whack(self, target, tie: bool):
        if self.attack > target.defense:
            target.health -= self.attack
            self.health -= target.attack
            if tie:
                print(f"Both fighters choose the same moment to strike")
            else:
                print(
                    f"{self.name} smacks {target.name} for {self.attack - target.defense}"
                )

    def print(self):
        print(
            "name: "
            + self.name
            + ", health: "
            + str(self.health)
            + ", attack: "
            + str(self.attack)
            + ", defense: "
            + str(self.defense)
            + ", speed: "
            + str(self.speed)
        )
