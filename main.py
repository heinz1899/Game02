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
    if element.id == 0:
        start_dice_animation(element)

# Dice
def start_dice_animation(element):
    global animate_dice
    pg.time.set_timer(pg.USEREVENT, 1000, True)
    animate_dice = True

def roll_dice():
    for element in group_elemente:
        if element.typ != "Dice" or element.selected:
            continue
        element.id = rnd.randint(1, 6)
        element.image_enabled = image_dice_enabled[element.id - 1]
        # element.image = image_dice_enabled[element.id - 1]
        element.image = element.image_enabled


# Games
games = {"none": None, "schocken": "schocken", "five_dices": "five_dices"}

game = games["schocken"]
image_dice_enabled = [pg.image.load(f"./Images/dices/{i + 1}_e.png") for i in range(6)]
image_dice_disabled = [pg.image.load(f"./Images/dices/{i + 1}_d.png") for i in range(6)]
if game == "schocken":
    schocken = Schocken()
    animate_dice = False
    schocken.add_elements(group_elemente)
    schocken.started = True

# ++++++++++++++++++++++++++++++++++ Game loop +++++++++++++++++++++++++++++++++++++++
run = True
text_counter = 0
while run:
    pg.draw.rect(screen, SCREEN_BACKGROUND_COLOR, [0, SCREEN_BORDER, SCREEN_WIDTH, SCREEN_HEIGHT])
    for event in pg.event.get():
        if event.type == pg.USEREVENT:
            animate_dice = False
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
    # +++++++++++++++++ Schocken ++++++++++++++++++
    if game == "schocken":
        schocken.background(screen)
        schocken.rules_draw(screen)
        if schocken.started:
            if animate_dice:
                roll_dice()

    group_elemente.draw(screen)
    pg.display.update()

    clock.tick(TICK)

pg.quit()
