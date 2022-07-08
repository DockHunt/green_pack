import pygame as pg
import currency, console, u_game_check, random

first_msg = u_game_check.U_Game_Check(
    """You wake up on the wrong side of the bed, the side covered in your blood.
            You feel the two 14 gauge syringe marks on your left deltoid."""
)

class U_Game:
    def __init__(self, resolution):
        self.screen, self.clock, self.console_font = U_Game.initialize(resolution)
        self.currs = dict()
        self.curr_check = {first_msg}

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

    def add_currency(self, currency: currency.Currency):
        self.currs[currency.name] = currency

    def write_to_console(self, console: console.Console):

        # NEEDS TO BE REWRITTEN
        for check in self.curr_check:
            if check.should_check:
                console.write(first_msg.complete())
        


