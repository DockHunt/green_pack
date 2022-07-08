#! /usr/bin/env python
""" 2nd version of Werewolf Pack Leader by Dock Hunter
Started: 9/16/2021
Last update: 1.1 on 24/6/22

A GUI idle game about growing a pack of lycathropes
"""
# import sys module
import pygame as pg
import sys, random
import body, console, counter, currency, u_button, u_game, u_image


def main():
    res = [1440, 1200]
    you = u_game.U_Game(res)

    # colors
    background_color = (32, 32, 64)
    button_normal = (50, 50, 50)  # dark gray
    button_hovered = (100, 100, 100)  # light gray
    text_color = (240, 240, 240)  # off white

    # set for objects to be drawn onscreen
    drawables = set()

    # initialize console
    cons = console.Console(pg.Rect(5, 5, 900, 400), you.console_font)
    drawables.add(cons)

    # currency: blood
    blood = currency.Currency("blood", "liters", 3.5)
    you.add_currency(blood)
    # counter: blood
    ctr1_rect = pg.Rect(910, 5, 90, 90)
    blood_ctr = counter.Counter(you.currs["blood"], ctr1_rect, you.console_font)
    max_blood = 6.5
    drawables.add(blood_ctr)
    # button: blood
    bld_btn_rect = pg.Rect(1005, 5, 270, 90)
    blood_btn = u_button.U_Button(bld_btn_rect, "eat red meat", you.console_font)
    drawables.add(blood_btn)

    # currency: nanobots
    nanobots = currency.Currency("nanobots", "μ", 48)
    you.add_currency(nanobots)
    # counter for nanobots
    ctr2_rect = pg.Rect(910, 100, 90, 90)
    nanobot_ctr = counter.Counter(you.currs["nanobots"], ctr2_rect, you.console_font)
    max_nanobots = 10 ** 6
    drawables.add(nanobot_ctr)
    # button: nanobots
    nano_btn_rect = pg.Rect(1005, 100, 270, 90)
    nanobot_btn = u_button.U_Button(nano_btn_rect, "condense iron", you.console_font)
    drawables.add(nanobot_btn)
    # body diagram
    bdy_rect = pg.Rect(5, 50, 600, 1000)
    our_body = body.Body(bdy_rect)
    drawables.add(our_body)

    max_ticker = 100
    CHECK_CONSOLE_TICKER = 100
    ticker = max_ticker

    while True:
        for event in pg.event.get():

            # if user types QUIT then the screen will close
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            """     CHECK IF SONSOLE CLICKEED AND PRINT TO CONSOLE
            if event.type == pg.MOUSEBUTTONDOWN:
                if cons.rect.collidepoint(event.pos):
                    cons.curr_text = "new line who clicked"
            """
            if event.type == pg.MOUSEBUTTONDOWN:
                if (
                    blood_btn.rect.collidepoint(event.pos)
                    and you.currs["blood"]._quantity < max_blood
                ):
                    you.currs["blood"].set_quantity(you.currs["blood"]._quantity + 0.1)

                if (
                    nanobot_btn.rect.collidepoint(event.pos)
                    and you.currs["blood"]._quantity > 5
                ):
                    you.currs["nanobots"].set_quantity(
                        you.currs["nanobots"]._quantity
                        + (you.currs["blood"]._quantity - 3) / 3
                    )
                    you.currs["blood"].set_quantity(3)

            if event.type == pg.KEYDOWN:

                # Check for backspace
                if event.key == pg.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    cons.curr_text = cons.curr_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    cons.curr_text += event.unicode

        # it will set background color of screen
        you.screen.fill(background_color)

        for drawable in drawables:
            drawable.draw(you.screen)
        pg.display.update()

        ticker = ticker - 1
        you.write_to_console(cons)
        if ticker <= 0:
            ticker = max_ticker
            if blood._quantity > max_blood:
                blood.set_quantity(blood._quantity * 0.98)
            else:
                blood.set_quantity(blood._quantity * 1.1)

            if nanobots._quantity > max_nanobots:
                nanobots.set_quantity(nanobots.quantity * 0.999)
            else:
                if nanobots._quantity > max_nanobots * 0.9:
                    nanobots.set_quantity(nanobots._quantity - 1)
                    nanobots.set_quantity(nanobots._quantity + random.randint(20, 39))

        # clock.tick(60) means that for every second at most
        # 60 frames should be passed.
        you.clock.tick(30)


# Execute Game
if __name__ == "__main__":
    args = sys.argv[1:]
    main()
