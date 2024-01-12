import pygame as pg
from elements import Element

# from pygame.sprite import Group
from constants import BOARD_FONT
from constants import SCREEN_BORDER, SCREEN_WIDTH
from random import randint
from game_text import rules


pg.init()


class Element(pg.sprite.Sprite):
    def __init__(self, number: int, typ: any, image: str, pos: list, enabled: bool) -> any:
        super().__init__()
        self.id = number
        self.typ = typ
        self.image_enabled = pg.image.load(image + '_e.png')
        self.image_disabled = pg.image.load(image + '_d.png')
        self.enabled = enabled
        self.image = self.image_enabled.copy() if enabled else self.image_disabled.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.selected = False


class Schocken:
    def __init__(self) -> None:
        self.dice_number = 3
        self.rules = rules["schocken"]
        self.started = False
        self.font_size = 32
        self.font = pg.font.Font(BOARD_FONT, self.font_size)
        self.path = "Images/dices/"
        # self.image_dices_e = [pg.image.load(f"{self.path}{i + 1}_e.png") for i in range(6)]
        # self.image_dices_d = [pg.image.load(f"{self.path}{i + 1}_d.png") for i in range(6)]
        self.group_elements = pg.sprite.Group()

    def rules_draw(self, surface):
        font_size = self.font_size
        line_space = 0

        rules_rect = pg.Surface((SCREEN_WIDTH, SCREEN_BORDER))
        rules_rect.set_alpha(150)
        rules_rect.fill((255, 255, 200))
        surface.blit(rules_rect, (0, 0))

        for i in range(len(self.rules)):
            txt = self.font.render(self.rules[i], True, "black")
            surface.blit(txt, (50, (60 + line_space)))
            line_space += font_size

    def dices(self):
        for i in range(1, 4):
            pos = (445 + (90 * i - 1), 450)
            self.group_elements.add(Element(i, "dices", f"{self.path}{i}", pos, True))

    def draw(self, surface):
        self.dices()
        self.group_elements.draw(surface)

        return None
