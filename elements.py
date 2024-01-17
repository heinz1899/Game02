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

    def change_enabled(self, enable_status):
        self.enabled = enable_status
        self.image = self.image_enabled.copy() if self.enabled else self.image_disabled.copy()
