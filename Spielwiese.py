import pygame
from schocken import Element


pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
path = "Images/dices/"

group_elemente = pygame.sprite.Group()

for i in range(3):
    pos = (500 + 90 * i, 100)
    group_elemente.add(Element(i, "Wüfel", f"{path}{i + 1}", pos, True))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    group_elemente.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
