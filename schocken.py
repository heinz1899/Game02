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

    def result(self, wurf: list) -> tuple[int, int]:
        wurf = sorted(wurf, reverse=True)
        if wurf == [1, 1, 1]:
            return 0, None  # schock aus
        elif wurf[1] == 1:
            summe = sum(wurf) - 2
            return 1, summe  # schock
        elif len(set(wurf)) == 1:
            return 2, sum(wurf) // 3  # general
        elif wurf[0] == wurf[1] + 1 and wurf[1] == wurf[2] + 1:
            return 3, sum(wurf)  # Number
        else:
            summe = int(f"{wurf[0]}{wurf[1]}{wurf[2]}")
            return 4, summe

    def render_result(self,render_x, render_y, group, d_counter, surface, player):
        w = [element.id for element in group if element.typ == "Dice"]
        wurf = sorted(w, reverse=True)
        wurf_count = {1: "ersten", 2: "zweiten", 3: "dritten"}
        erg_typ, summe = self.result(wurf)

        if erg_typ == 4:
            result_txt = f"Zahl: {wurf[0]} {wurf[1]}{wurf[2]} im {wurf_count[d_counter]} Wurf"
        if erg_typ == 3:
            wurf = sorted(wurf, reverse=False)
            result_txt = f"Straße: {wurf[0]} {wurf[1]} {wurf[2]} im {wurf_count[d_counter]} Wurf"
        if erg_typ == 2:
            result_txt = f"General {summe} im {wurf_count[d_counter]} Wurf"
        if erg_typ == 1:
            result_txt = f" Schock {summe} im {wurf_count[d_counter]} Wurf"
        if erg_typ == 0:
            result_txt = "Schock AUS - Du hast die Runde gewonnen"

        text = pg.font.SysFont("arial", 24).render(result_txt, True, "black")
        name = pg.font.SysFont("arial", 30).render(player.name, True, "blue")
        surface.blit(name, (render_x, render_y))
        surface.blit(text, (render_x, render_y + 40))

    def save_dice_result(self, group, d_counter, player):
        """Output: erg_Typ, Summe, Anzahl Würfe"""
        w = [element.id for element in group if element.typ == "Dice"]
        wurf = sorted(w, reverse=True)
        erg_typ, summe = self.result(wurf)
        # points
        if erg_typ == 4:
            points = 1
        elif erg_typ == 3:
            points = 2
        elif erg_typ == 2:
            points = 3
        elif erg_typ == 1 and summe > 1:
            points = summe
        elif erg_typ == 0:
            points = 13

        result = {"typ": erg_typ, "summe": summe, "number_of_dice_rolls": d_counter, "points": points}
        return result

    def computer_play(self):
        pass
