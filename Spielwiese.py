import pygame
import board_text
from games import schocken_info


pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
textfont = pygame.font. SysFont("monospace", 24)
text = {
    "start": "Aller Anfang ist schwer!"
}
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #text_tbd = textfont.render(board_text.board_text["schocken"], True, "white")
    # text_tbd = textfont.render(schocken_info.text, True, "white")
    # screen.blit(text_tbd, (50, 50))
    schocken_info.draw(screen)




    pygame.display.flip()
    clock.tick(60)

pygame.quit()
