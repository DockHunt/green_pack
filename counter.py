import pygame as pg
import currency


class Counter:
    def __init__(self, currency: currency, rect, font):
        self.currency = currency
        self.rect = rect
        self.text_color = (200, 200, 200)
        self.bg_color = (16, 32, 16)
        self._font = font

    def get_font(self):
        return self._font

    def draw(self, surface, alpha=255):
        # draw rectangle and argument passed which should
        # be on screen
        pg.draw.rect(surface, self.bg_color, self.rect, 0, 3)

        text_surface = self._font.render(
            str("{:.2f}".format(self.currency._quantity)), True, self.text_color
        )

        # render at position stated in arguments
        surface.blit(
            text_surface,
            (
                self.rect.x + (self.rect.w / 2) - text_surface.get_width() / 2,
                self.rect.y + (self.rect.h / 2) - text_surface.get_height() / 2,
            ),
        )

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        # pg.display.flip()
