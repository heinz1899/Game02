import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGTH, SCREEN_TITLE, SCREEN_BACKGROUND_COLOR, SCREEN_BORDER, TICK, DIALOG_FONT
from dialog import create_message

pygame.init()
clock = pygame.time.Clock()

# Screen
pygame.display.set_caption(SCREEN_TITLE)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGTH])
screen_background = pygame.image.load("./Images/hintergrund.png")


def draw_screen() -> None:
    screen.blit(screen_background, (0, 0))
    pygame.display.update()



font = pygame.font.Font(DIALOG_FONT, 24)
snip = font.render("", True, "white")
text_counter = 0
text_speed = 3
message = "Heiner ist der Beste"





# ++++++++++++++++++++++++++++++++++ Game loop +++++++++++++++++++++++++++++++++++++++
run = True
while run:
    pygame.draw.rect(screen, SCREEN_BACKGROUND_COLOR, [0, SCREEN_BORDER, SCREEN_WIDTH, SCREEN_HEIGTH])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    message, new_input = create_message("ja")
    if text_counter < text_speed * len(message):
        text_counter += 1

    snip = font.render(message[0 : text_counter // text_speed], True, "white")
    screen.blit(snip, (20, SCREEN_BORDER))

    draw_screen()
    clock.tick(TICK)

pygame.quit()
