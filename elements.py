import pygame as pg

pg.init()


class Element(pg.sprite.Sprite):
    def __init__(self, number: int, typ: str, image: str, pos: tuple, enabled: bool) -> any:
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
