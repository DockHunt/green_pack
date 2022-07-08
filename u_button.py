import pygame as pg
import counter


class U_Button:
    def __init__(self, rect: pg.Rect, phrase: str, font):
        self.rect = rect
        self.writing = phrase
        self.text_color = (200, 200, 200)
        self.bg_color = (16, 32, 16)
        self._font = font

    def draw(self, surface, alpha=255):
        # draw rectangle and argument passed which should
        # be on screen
        pg.draw.rect(surface, self.bg_color, self.rect, 0, 3)

        text_surface = self._font.render(self.writing, True, self.text_color)

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
