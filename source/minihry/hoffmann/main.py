import pygame
import sys
import random

pygame.init()

rozliseni_okna = (1280, 900)
okno = pygame.display.set_mode(rozliseni_okna)

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    okno.fill((50, 50, 50))

    pygame.display.update()