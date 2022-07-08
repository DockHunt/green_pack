#!/usr/bin/env python
""" Werewolf Pack Leader by Dock Hunter
Started: 9/16/2021
Last update: 1.0 on 9/16/22

A GUI idle game about growing a pack of lycathropes
"""

# import modules
import pygame as pg
import sys
from pygame.locals import *
import button
import images

# screen resolution
screen_res = (1440, 1200)

# colors
background = (32, 32, 64)  # dark blue
button_normal = (50, 50, 50)  # dark gray
button_hovered = (100, 100, 100)  # light gray
text_color = (240, 240, 240)  # off white


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


def initialize(resolution):
    pg.init()
    if not pg.font:
        print("warning: font failed to start up")

    # initialize window and settings
    screen = pg.display.set_mode(resolution)
    pg.display.set_caption("The Green Pack")

    return screen


def main():
    screen = initialize(screen_res)
    width = screen.get_width()
    height = screen.get_height()
    pg.mouse.set_visible(1)
    clock = pg.time.Clock()
    font = "Corbel"
    normal_font = pg.font.SysFont(font, 32)

    resources = []

    meat = Resource("meat", 0, font, (20, 40))
    resources.append(meat)
    wolves = Resource("wolves", 1, font, (100, 40))
    resources.append(wolves)
    grn_ears = Resource("green ears", 0, font, (180, 40))
    resources.append(grn_ears)
    max_ticker = 100
    ticker = max_ticker

    # UI - static elements

    button_image = pg.image.load("images/button_v1.png").convert_alpha()
    button_image = pg.image.load("images/button_v1.png").convert_alpha()

    # buttons
    button_v1 = button.Button(200, 200, button_image, 1)
    buy_wolf_label = normal_font.render("feed the pack", True, text_color)
    buy_wolf_button = pg.Rect(20, 80, 150, 30)

    buy_grn_ear_label = normal_font.render("cull the weak", True, text_color)
    buy_grn_ear_button = pg.Rect(20, 120, 150, 30)

    labels = []

    for res in resources:
        x, y = res.counter_loc
        labels.append([res.get_label(), (x, y - 20)])

    # meat_label = normal_font.render('meat', True, text_color)
    # meat_label_loc = (20, 20)

    # wolf_label = normal_font.render('wolves', True, text_color)
    # wolf_label_loc = (100, 20)

    # grn_ear_label = normal_font.render('green ears', True, text_color)
    # grn_ear_label_loc = (180, 20)

    # UI - locations of dynamic elements
    # meat_counter_loc = (20, 40)
    wolf_counter_loc = (100, 40)
    grn_ear_counter_loc = (180, 40)

    while True:

        for ev in pg.event.get():

            if ev.type == pg.QUIT:
                pg.quit()

            # stores mouse vars
            if ev.type == pg.MOUSEBUTTONDOWN:

                # if mouse is clicked on button, buy wolves
                if button_v1.rect.collidepoint(ev.pos):
                    resources[1].quantity = (
                        resources[1].quantity + resources[0].quantity // 5
                    )

                if buy_wolf_button.collidepoint(ev.pos):
                    resources[1].quantity = (
                        resources[1].quantity + resources[0].quantity // 5
                    )
                    resources[0].quantity = resources[0].quantity % 5
                elif buy_grn_ear_button.collidepoint(ev.pos):
                    resources[2].quantity = (
                        resources[2].quantity + resources[1].quantity // 10
                    )
                    resources[1].quantity = resources[1].quantity // 2

        screen.fill(background)

        counters = []

        for res in resources:
            counters.append(
                normal_font.render(str(int(res.quantity)), True, text_color)
            )
            counters.append(res.counter_loc)

        # meat_counter = normal_font.render(str(int(meat)), True, text_color)
        # wolf_counter = normal_font.render(str(int(wolves)), True, text_color)
        # grn_ear_counter = normal_font.render(str(int(grn_ears)), True, text_color)

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pg.mouse.get_pos()

        button_v1.draw(screen)

        # if mouse is hovered on a button it
        # changes to lighter shade
        if buy_wolf_button.collidepoint(mouse):
            pg.draw.rect(screen, button_hovered, buy_wolf_button)
            pg.draw.rect(screen, button_normal, buy_grn_ear_button)

        elif buy_grn_ear_button.collidepoint(mouse):
            pg.draw.rect(screen, button_normal, buy_wolf_button)
            pg.draw.rect(screen, button_hovered, buy_grn_ear_button)

        else:
            pg.draw.rect(screen, button_normal, buy_wolf_button)
            pg.draw.rect(screen, button_normal, buy_grn_ear_button)

        for label in labels:
            screen.blit(label[0], label[1])

        # while labels:
        #    screen.blit(labels.pop(0), labels.pop(0))

        # screen.blit(meat_label, meat_label_loc)
        # screen.blit(wolf_label, wolf_label_loc)
        # screen.blit(grn_ear_label, grn_ear_label_loc)

        while counters:
            screen.blit(counters.pop(0), counters.pop(0))
        # screen.blit(meat_counter, meat_counter_loc)
        # screen.blit(wolf_counter, wolf_counter_loc)
        # screen.blit(grn_ear_counter, grn_ear_counter_loc)

        screen.blit(buy_wolf_label, buy_wolf_button)
        screen.blit(buy_grn_ear_label, buy_grn_ear_button)

        pg.display.update()

        ticker = ticker - 1
        if ticker <= 0:
            ticker = max_ticker
            resources[0].quantity = resources[0].quantity + resources[1].quantity

        clock.tick(60)


# Execute Game
if __name__ == "__main__":
    args = sys.argv[1:]
    main()
