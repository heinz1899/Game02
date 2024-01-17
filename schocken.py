import pygame as pg
from elements import Element
from constants import BOARD_FONT
from constants import SCREEN_BORDER, SCREEN_WIDTH
from game_text import rules


pg.init()


class Schocken:
    def __init__(self) -> None:
        self.dice_number = 3
        self.rules = rules["schocken"]
        self.started = False
        self.font_size = 32
        self.font = pg.font.Font(BOARD_FONT, self.font_size)
        self.path = 'Images/'


    def background(self, surface):
        schocken_rect = pg.Surface((SCREEN_WIDTH, SCREEN_BORDER))
        schocken_rect.set_alpha(150)
        schocken_rect.fill((100, 255, 100))
        surface.blit(schocken_rect, (0, 0))

    def rules_draw(self, surface: pg.surface) -> None:
        font_size = self.font_size
        line_space = 0
        for i in range(len(self.rules)):
            txt = self.font.render(self.rules[i], True, "black")
            surface.blit(txt, (50, (60 + line_space)))
            line_space += font_size

    def add_elements(self, group):
        for i in range(1, 4):
            pos = (445 + (90 * i - 1), 100)
            group.add(Element(i, "Dice", f"Images/dices/{i}", pos, True))

        for n in range(3):
            pos = [(200, 100), (815, 100), (506, 300)]
            enabled = n == 0
            group.add(Element(n, 'Button', f'{self.path}buttons/Button{n}', pos[n], enabled))







    def draw(self, surface: pg.surface) -> None:
        self.group_elements.draw(surface)
