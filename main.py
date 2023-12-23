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
#snip2 = font.render("", True, "white")
text_counter = 0

text_speed = 10

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

    messages, new_input = create_message("Nein", level)
    if text_counter == 0:
        snip2 = font.render("", True, "white")


    if text_counter < (text_speed * (len(messages[0])) + (text_speed * len(messages[1]))):
        text_counter += 1

        snip1 = font.render(messages[0][0 : text_counter // text_speed], True, "white")

    len_multiplicate_speed = text_speed * len(messages[0])
    if (text_counter >= len_multiplicate_speed) and (
        text_counter < (text_speed * (len(messages[0])) + (text_speed * len(messages[1])))
    ):

        if text_counter - len_multiplicate_speed < (text_speed * len(messages[1])):
            text_counter += 1

        snip2 = font.render(messages[1][0 : ((text_counter) - len_multiplicate_speed) // text_speed], True, "white")

    screen.blit(snip1, (20, (SCREEN_BORDER)))
    screen.blit(snip2, (20, (SCREEN_BORDER + 25)))


    draw_screen()
    clock.tick(TICK)

pygame.quit()
