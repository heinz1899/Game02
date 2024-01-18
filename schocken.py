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
        # Dice
        for i in range(1, 4):
            pos = (445 + (90 * i - 1), 100)
            group.add(Element(i, "Dice", f"Images/dices/{i}", pos, True))
        # Button
        button_pos = {"Würfeln": (815, 100), "OK": (1000, 100), "Neues Spiel": (506, 300)}
        for n, button in enumerate(button_pos):
            # pos = [(200, 100), (815, 100), (506, 300)]
            enabled = button != "Neues Spiel"
            group.add(Element(n, 'Button', f'{self.path}buttons/Button{n}', button_pos[button], enabled))

    def ergebnis_typ_ermitteln(self, wurf):
        if wurf == [1, 1, 1]:
            return "schock_aus"
        elif sorted(wurf)[1] == 1:
            return "schock"
        elif len(set(wurf)) == 1:
            return "general"
        elif sorted(wurf)[0] == sorted(wurf)[1] - 1 and sorted(wurf)[1] == sorted(wurf)[2] - 1:
            return "street"
        else:
            return "number"

    def punkte_ermitteln(self, ergebnis_typ, group, d_counter):
        ergebnis_typen = {"schock_aus": 0, "schock": 1, "general": 2, "street": 3, "number": 4}
        w = [element.id for element in group if element.typ == "Dice"]
        wurf = sorted(w, reverse=True)
        print(wurf)
        print(wurf[0])
        wurf_count = {1: "ersten", 2: "zweiten", 3: "dritten"}
        erg_typ = ergebnis_typen[ergebnis_typ]

        if erg_typ == 4:
            return f"Zahl: {wurf[0]} {wurf[1]}{wurf[2]} im {wurf_count[d_counter]} Wurf"
        if erg_typ == 3:
            return wurf
        if erg_typ == 2:
            return wurf
        if erg_typ == 1:
            return wurf


test = Schocken()
print(test.ergebnis_typ_ermitteln([4, 2, 3]))
