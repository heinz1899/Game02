import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGTH = 892
SCREEN_TITLE = "Spiel"
SCREEN_BACKGROUND_COLOR = (50, 50, 50)
SCREEN_BORDER = 600
TICK = 60


pygame.init()
clock = pygame.time.Clock()

# Screen
pygame.display.set_caption(SCREEN_TITLE)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGTH])
screen_background = pygame.image.load("./Images/hintergrund.png")

font = pygame.font.Font(None, 24)
snip1 = font.render("", True, "white")
text_counter = 0
text_speed = 3
level = 1


def draw_screen() -> None:
    pygame.display.update()


# ++++++++++++++++++++++++++++++++++ Game loop +++++++++++++++++++++++++++++++++++++++
run = True
while run:
    pygame.draw.rect(screen, (150, 50, 0), [0, 0, SCREEN_WIDTH, SCREEN_HEIGTH])
    pygame.draw.rect(screen, SCREEN_BACKGROUND_COLOR, [0, SCREEN_BORDER, SCREEN_WIDTH, SCREEN_HEIGTH])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Die messages sollen später die Reaktion auf einen user-input sein. new input ist True, wenn eine weitere User-Eingabe erfolgen soll
    # messages, new_input = create_message("ja", level)
    messages = ["Das ist die erste Zeile. Die soll fertig geschrieben sein", "...bevor die zweite Zeile erscheint."]

    messages_lens = [len(m) for m in messages]
    len_all_messages = sum(messages_lens)
    text_counter_max = len_all_messages * text_speed

    # snips enthält einen Eintrag für jedes Elemten der Liste messages
    #snips = [font.render(message[0 : (text_counter // text_speed) + 1], True, "white") for message in messages]
    # snips enthält einen Eintrag für jedes Elemten der Liste messages
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

    for snip in snips:  # TODO Die Zeilen sollen nacheinander erscheinen
        screen.blit(snip, (20, (SCREEN_BORDER + line_spacing)))
        line_spacing += 25

    print(f"a: {messages_lens}, b: {len_all_messages}, c: {text_counter_max}")
    draw_screen()
    clock.tick(TICK)

pygame.quit()
