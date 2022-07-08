import pygame as pg


class Currency:
    def __init__(self, name, units, init_quantity):
        self.name = name
        self.units = units
        self._quantity = init_quantity

    def set_quantity(self, new_quantity):
        self._quantity = new_quantity
