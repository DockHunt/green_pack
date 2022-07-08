#!/usr/bin/env python
import pygame as pg


class Console:
    def __init__(self, cons_rect, font: pg.font):
        self.rect = cons_rect
        self.curr_text = ""
        self.text_color = (200, 200, 200)
        self.bg_color = (24, 24, 24)
        self._font = font

    def draw(self, surface, alpha=255):
        # draw rectangle and argument passed which should
        # be on screen
        pg.draw.rect(surface, self.bg_color, self.rect)

        words = [
            word.split(" ") for word in self.curr_text.splitlines()
        ]  # 2d array where each row is a list of words
        space = self._font.size(" ")[0]  # width of a space
        max_width, max_height = self.rect.w, self.rect.h
        x, y = self.rect.left + 5, self.rect.top + 5
        for line in words:
            for word in line:
                word_surface = self._font.render(word, 0, self.text_color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = 5  # reset the x
                    y += word_height  # start new row
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = 5  # reset the x
            y += word_height  # start new row

        """
        text_surface = self._font.render(self.curr_text, True, self.text_color)

        # render at position stated in arguments
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        """

    def write(self, new_text):
        self.curr_text = self.curr_text + "\n" + new_text
