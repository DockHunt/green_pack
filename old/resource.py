import pygame as pg


class Resource:
    """handles the labels and counters of a given reosurece, like meat or runes"""

    def __init__(self, name, quantity, font, counter_location):
        self.name = name
        self.quantity = int(quantity)
        self.font = pg.font.SysFont(font, 32)
        self.counter_loc = counter_location

    def get_label(self):
        return self.font.render(self.name, True, text_color)

    def get_counter(self):
        return self.font.render(str(int(self.quantity)), True, text_color)
