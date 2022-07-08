#!/usr/bin/env python
import pygame as pg

class U_Image:
    def __init__(self, rect: pg.Rect, image_location):
        self.rect = rect
        self.image = pg.image.load(image_location).convert_alpha()

    def draw(self, surface, alpha=255):

        alphable_surface = pg.Surface((self.rect.w, self.rect.h))
        alphable_surface.set_alpha(int(alpha))
        surface.blit(self.image, (self))
