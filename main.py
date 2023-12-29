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
text_counter = 0
text_speed = 5
level = 0
user_communication = True
player = "user"
input_text = f"{player}>: "
player_text = ""


def draw_screen() -> None:
    screen.blit(screen_background, (0, 0))
    pygame.display.update()


# ++++++++++++++++++++++++++++++++++ Game loop +++++++++++++++++++++++++++++++++++++++
run = True
text_counter = 0
while run:
    pygame.draw.rect(screen, SCREEN_BACKGROUND_COLOR, [0, SCREEN_BORDER, SCREEN_WIDTH, SCREEN_HEIGTH])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # for user input
        #if user_communication:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                print(f"input_text: {input_text}")
                player_text = input_text
                level += 1
                create_message(player_text, level)

            else:
                input_text += event.unicode

    # +++++++++ User communication start ++++++++++++

    messages, new_input = create_message(player_text, level)

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

    line_spacing = 0

    for snip in snips:
        screen.blit(snip, (20, (SCREEN_BORDER + line_spacing)))
        line_spacing += 25

    new_input = True
    if new_input and text_counter >= (len_all_messages * text_speed):
        input_surface = font.render(input_text, True, (40, 150, 0))
        screen.blit(input_surface, (20, SCREEN_BORDER + line_spacing))


    # +++++++++ User communication end ++++++++++++

    draw_screen()
    clock.tick(TICK)

pygame.quit()
