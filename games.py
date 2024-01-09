import pygame
from constants import BOARD_FONT
from random import randint
from game_text import rules
from constants import SCREEN_BORDER, SCREEN_WIDTH



pygame.init()


class Schocken:
    def __init__(self) -> None:
        self.dice_number = 3
        self.dice_sides = 6
        self.rules = rules["schocken"]
        self.font_size = 32
        self.font = pygame.font.Font(BOARD_FONT, self.font_size)

    def roll_dice(self):
        return randint(1, self.dice_sides)

    def rules_draw(self, surface):
        font_size = self.font_size
        line_space = 0

        rules_rect = pygame.Surface((SCREEN_WIDTH, SCREEN_BORDER))
        rules_rect.set_alpha(150)
        rules_rect.fill((255, 255, 200))
        surface.blit(rules_rect, (0, 0))

        for i in range(len(self.rules)):
            txt = self.font.render(self.rules[i], True, "black")
            surface.blit(txt, (50, (60 + line_space)))
            line_space += font_size

        return None


schocken = Schocken()
