import pygame as pg
import console


class U_Game_Check:
    def __init__(self, text: str):
        self.text = text
        self.should_check = True
        self.completed = False

    def complete(self):
        self.should_check = False
        self.completed = True
        return self.text
