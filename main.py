import pygame
from userCommunication import create_message
from constants import SCREEN_WIDTH, SCREEN_HEIGTH, SCREEN_TITLE, SCREEN_BACKGROUND_COLOR, SCREEN_BORDER, TICK, DIALOG_FONT


pygame.init()
clock = pygame.time.Clock()

# Screen
pygame.display.set_caption(SCREEN_TITLE)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGTH])
screen_background = pygame.image.load("./Images/hintergrund.png")

font = pygame.font.Font(DIALOG_FONT, 24)
snip1 = font.render("", True, "white")
text_counter = 0
text_speed = 5
level = 1


def draw_screen() -> None:
    screen.blit(screen_background, (0, 0))
    pygame.display.update()


# ++++++++++++++++++++++++++++++++++ Game loop +++++++++++++++++++++++++++++++++++++++
run = True
while run:
    pygame.draw.rect(screen, SCREEN_BACKGROUND_COLOR, [0, SCREEN_BORDER, SCREEN_WIDTH, SCREEN_HEIGTH])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # User communication
    messages, new_input = create_message("äh", level)
    snips = []

    len_all_messages = 0

    # snips enthält einen Eintrag für jedes Elemten der Liste messges
    snips = [font.render(message[0 : (text_counter // text_speed) + 1], True, "white") for message in messages]

    # errechnet die Gesamtlänge aller Texte
    for message in messages:
        len_all_messages += len(message)
    # text_counter muss weiterlaufen, bis der gesamte Text ausgegeben wurde
    if text_counter < (len_all_messages * text_speed):
        text_counter += 1

    len_multiplicate_speed = text_speed * len(messages[0])
    if (text_counter >= len_multiplicate_speed) and (
        text_counter < (text_speed * (len(messages[0])) + (text_speed * len(messages[1])))
    ):
        if text_counter - len_multiplicate_speed < (text_speed * len(messages[1])):
            text_counter += 1

    line_spacing = 0
    for snip in snips:  # TODO Die Zeilen sollen nacheinander erscheinen
        screen.blit(snip, (20, (SCREEN_BORDER + line_spacing)))
        line_spacing += 25

    draw_screen()
    clock.tick(TICK)

pygame.quit()
