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
        self.draw = False

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

    def ergebnis_typ(self, wurf: list) -> tuple[str, int]:
        wurf = sorted(wurf, reverse=True)
        if wurf == [1, 1, 1]:
            return "schock_aus", None
        elif wurf[1] == 1:
            summe = sum(wurf) - 2
            return "schock", summe
        elif len(set(wurf)) == 1:
            return "general", sum(wurf)
        elif wurf[0] == wurf[1] + 1 and wurf[1] == wurf[2] + 1:
            return "street", sum(wurf)
        else:
            summe = int(f"{wurf[2]}{wurf[1]}{wurf[0]}")
            return "number", summe

    def render_ergebnis(self, group, d_counter, surface, player):
        w = [element.id for element in group if element.typ == "Dice"]
        wurf = sorted(w, reverse=True)
        wurf_count = {1: "ersten", 2: "zweiten", 3: "dritten"}
        erg_typ, summe = self.ergebnis_typ(wurf)

        if erg_typ == "number":
            ergebnis_txt = f"Zahl: {wurf[0]} {wurf[1]}{wurf[2]} im {wurf_count[d_counter]} Wurf"
        if erg_typ == "street":
            wurf = sorted(wurf, reverse=False)
            ergebnis_txt = f"Straße: {wurf[0]} {wurf[1]} {wurf[2]} im {wurf_count[d_counter]} Wurf"
        if erg_typ == "general":
            ergebnis_txt = f"General {wurf[0]} im {wurf_count[d_counter]} Wurf"
        if erg_typ == "schock":
            ergebnis_txt = f" Schock {summe} im {wurf_count[d_counter]} Wurf"
        if erg_typ == "schock_aus":
            ergebnis_txt = "Schock AUS - Du hast die Runde gewonnen"

        text = pg.font.SysFont("arial", 24).render(ergebnis_txt, True, "black")
        name = pg.font.SysFont("arial", 30).render(player.name, True, "red")
        surface.blit(name, (50, 10))
        surface.blit(text, (50, 50))
