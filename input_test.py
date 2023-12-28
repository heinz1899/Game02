import pygame
import sys

pygame.init()
base_font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 800])
player = "user"
input_text = f"{player}: "
user_input = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode


    if user_input:
        input_surface = base_font.render(input_text, True, (40, 150, 0))
        screen.blit(input_surface, (0, 100))

    pygame.display.flip()
    clock.tick(60)
