import pygame as pg
from user_communication import create_message
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_BACKGROUND_COLOR, SCREEN_BORDER, TICK
from constants import DIALOG_FONT, LINE_SPACING
from player import player
from schocken import Schocken
import random as rnd


pg.init()
clock = pg.time.Clock()
group_elemente = pg.sprite.Group()
pg.time.set_timer(pg.USEREVENT, 1000, True)

# Screen
pg.display.set_caption(SCREEN_TITLE)
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen_background_start = pg.image.load("./Images/hintergrund.png")

# user communication
user_communication = True
font = pg.font.Font(DIALOG_FONT, 24)
text_counter = 0
text_speed = 3
communication_counter = 0
next_message = 0
new_input = True  # Bei True ist user-input möglich
input_text = ""  # verändert sich während der Eingabe
player_text = ""  # input nach Bestätigung mit Return


# Mouse-Events
def clicked_button(element):
    if element.id == 0:  # Button "würfeln"
        start_dice_animation() # (element)


def clicked_dice(element):  # schocken
    element.selected = not element.selected
    element.image = image_dice_disabled[element.id - 1] if element.selected else image_dice_enabled[element.id - 1]


# Dice
def start_dice_animation(): # (element)
    global animate_dice
    global dice_counter
    pg.time.set_timer(pg.USEREVENT, 1000, True)
    animate_dice = True
    dice_counter += 1
    if dice_counter >= 3:
        element.change_enabled(False)


def roll_dice():
    for element in group_elemente:
        if element.typ != "Dice" or element.selected:
            continue
        element.id = rnd.randint(1, 6)
        element.image_enabled = image_dice_enabled[element.id - 1]
        # element.image = image_dice_enabled[element.id - 1]
        element.image = element.image_enabled


# Games
games = {"none": "none", "schocken": "schocken", "five_dices": "five_dices"}
game = games["none"]
# ------------------------------------------
schocken = Schocken()
schocken_started = False
animate_dice = False
dice_counter = 1  # zum zählen der Würfe
image_dice_enabled = [pg.image.load(f"./Images/dices/{i + 1}_e.png") for i in range(6)]
image_dice_disabled = [pg.image.load(f"./Images/dices/{i + 1}_d.png") for i in range(6)]
schocken.add_elements(group_elemente)
animate_dice = True


def start_schocken():
    global schocken_started
    global game
    global animate_dice
    start_dice_animation()  # first roll
    game = games["schocken"]
    schocken.started = True
    print("Schocken ist gestartet!")


# --------------------------------------------

# ++++++++++++++++++++++++++++++++++ Game loop +++++++++++++++++++++++++++++++++++++++
run = True
text_counter = 0
while run:
    # event handle
    pg.draw.rect(screen, SCREEN_BACKGROUND_COLOR, [0, SCREEN_BORDER, SCREEN_WIDTH, SCREEN_HEIGHT])
    for event in pg.event.get():
        if event.type == pg.USEREVENT:
            animate_dice = False
            schocken.draw = True
        if event.type == pg.QUIT:
            run = False
        if user_communication:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pg.K_RETURN:
                    player_text = input_text
                    text_counter = 0
                    communication_counter = next_message
                    input_text = ""
                    print(communication_counter)
                    if communication_counter == 4:
                        start_schocken()

                else:
                    input_text += event.unicode
        if event.type == pg.MOUSEBUTTONDOWN:
            point = pg.mouse.get_pos()
            for element in group_elemente:
                if not element.enabled or not element.rect.collidepoint(point):
                    continue
                else:
                    if element.typ == "Button":
                        clicked_button(element)
                        schocken.draw = True
                    if element.typ == "Dice":
                        clicked_dice(element)

    # +++++++++ User communication start ++++++++++++
    messages, new_input, next_message = create_message(player_text, communication_counter)

    messages_lens = [len(m) for m in messages]
    len_all_messages = sum(messages_lens)
    text_counter_max = len_all_messages * text_speed

    # snips enthält einen Eintrag für jedes Elemten der Liste messges
    snips = []
    characters_to_plot = text_counter // text_speed + 1
    for message in messages:
        if characters_to_plot > len(message):
            text = message
            characters_to_plot -= len(message)
        elif characters_to_plot > 0:
            text = message[:characters_to_plot]
            characters_to_plot = 0
        else:
            text = ""
        snips.append(font.render(text, True, "white"))

    # text_counter muss weiterlaufen, bis der gesamte Text ausgegeben wurde
    if text_counter < (len_all_messages * text_speed):
        text_counter += 1
    lines = 0
    for i, snip in enumerate(snips):
        screen.blit(snip, (20, (SCREEN_BORDER + (i * LINE_SPACING))))
        lines += 1

    #  input Prombt
    if new_input and text_counter >= (len_all_messages * text_speed):
        input_surface = font.render(f"{player.prompt} {input_text}", True, (40, 150, 0))
        screen.blit(input_surface, (20, SCREEN_BORDER + (LINE_SPACING * lines)))
        lines = 0

    # ++++++++++++++++++++++++++ User communication end +++++++++++++++++++++++++++

    # background picture
    screen.blit(screen_background_start, (40, 0))

    # +++++++++++++++++++++++++++++++++++ Games +++++++++++++++++++++++++++++++++++

    # ++++++++++ Schocken start
    if game == "schocken":
        schocken.background(screen)
        if schocken.started:
            if animate_dice:
                roll_dice()
        if event.type == pg.USEREVENT:
            animate_dice = False

        # else:
        #     schocken.rules_draw(screen)
        # +++++++++++ Schocken end

        group_elemente.draw(screen)
        if schocken.draw:
            schocken.render_ergebnis(group_elemente, dice_counter, screen, player)

    pg.display.update()
    clock.tick(TICK)

pg.quit()
