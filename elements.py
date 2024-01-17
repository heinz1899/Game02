import pygame as pg

pg.init()


class Element(pg.sprite.Sprite):
    def __init__(self, id: int, typ: str, image: str, pos: tuple, enabled: bool) -> None:
        super().__init__()
        self.id = id
        self.typ = typ
        self.image_enabled = pg.image.load(image + '_e.png')
        self.image_disabled = pg.image.load(image + '_d.png')
        self.enabled = enabled
        self.image = self.image_enabled.copy() if enabled else self.image_disabled.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.selected = False

    # def change_enabled(self, t):
    #     self.enabled = t
    #     self.image = self.image_e.copy() if enabled else self.image_d.copy()
