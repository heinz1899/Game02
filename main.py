import pygame as pg
from user_communication import create_message
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_BACKGROUND_COLOR, SCREEN_BORDER, TICK
from constants import DIALOG_FONT, LINE_SPACING
from player import player
from schocken import Schocken


pg.init()
clock = pg.time.Clock()

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
new_input = True  # Bei True ist user-input möglich
input_text = ""  # verändert sich während der Eingabe
player_text = ""  # input nach Bestätigung mit Return

# Games
group_elements = pg.sprite.Group()
games = {"none": None, "schocken": "schocken", "five_dices": "five_dices"}
game = games["schocken"]

# ++++++++++++++++++++++++++++++++++ Game loop +++++++++++++++++++++++++++++++++++++++
run = True
text_counter = 0
while run:
    pg.draw.rect(screen, SCREEN_BACKGROUND_COLOR, [0, SCREEN_BORDER, SCREEN_WIDTH, SCREEN_HEIGHT])
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        # for user input
        if user_communication:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pg.K_RETURN:
                    player_text = input_text
                    text_counter = 0
                    communication_counter += 1
                    input_text = ""
                else:
                    input_text += event.unicode

    # +++++++++ User communication start ++++++++++++
    messages, new_input = create_message(player_text, communication_counter)

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

    for i, snip in enumerate(snips):
        screen.blit(snip, (20, (SCREEN_BORDER + (i * LINE_SPACING))))

    #  input Prombt
    if new_input and text_counter >= (len_all_messages * text_speed):
        input_surface = font.render(f"{player.prompt} {input_text}", True, color=(40, 150, 0))
        screen.blit(input_surface, (20, SCREEN_BORDER + LINE_SPACING))

    # ++++++++++++++++++++++++++ User communication end +++++++++++++++++++++++++++

    # background picture
    screen.blit(screen_background_start, (40, 0))

    # +++++++++++++++++++++++++++++++++++ Games +++++++++++++++++++++++++++++++++++
    # +++++++++++++++++ Schocken ++++++++++++++++++
    if game == "schocken":
        schocken = Schocken()
        if not schocken.started:
            # schocken.rules_draw(screen)
            schocken.draw(screen)



    pg.display.update()

    clock.tick(TICK)

pg.quit()
