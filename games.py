import pygame
from board_text import board_text
from constants import BOARDS_FONT

pygame.init()


class Game:
    def __init__(self, x: int, y: int, height: int, width: int, text: list) -> None:
        self.rect = pygame.Rect(x, y, height, width)
        self.text = text
        self.font = pygame.font.Font(BOARDS_FONT, 24)
        self.x = x
        self.y = y

    def info_draw(self, surface):
        line_space = 0
        for i in range(len(self.text)):
            img = self.font.render(self.text[i], True, "black")
            surface.blit(img, (50, (60 + line_space)))
            line_space += 32



schocken = Game(0, 0, 100, 200, board_text["schocken"])
