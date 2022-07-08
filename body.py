#!/usr/bin/env python
from random import randint
import pygame as pg
import u_image

class Body:
    def __init__(self, rect: pg.Rect):
        self.rect = rect
        self.brain = pg.image.load('images/frontier_psychology2.png').convert_alpha()
        self.nerves = pg.image.load('images/nerves.png').convert_alpha()
        self.bloodstream = pg.image.load('images/phlebotomy.png').convert_alpha()

    def draw(self, surface, alpha=255):
        
        alphable_surface = pg.Surface((self.rect.w + 5, self.rect.h + 5))
        alphable_surface.set_alpha(255)
        surface.blit(self.brain, (self.rect.move(randint(-2, 2), randint(-2, 2) - 110)))
        surface.blit(self.nerves, (self.rect.move(randint(-2, 2), randint(-2, 2) - 110)))
        surface.blit(self.bloodstream, (self.rect.move(randint(-2, 2), randint(-2, 2) - 110)))