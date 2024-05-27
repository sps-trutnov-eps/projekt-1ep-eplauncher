import pygame
import sys
import random

#platformy padají dolů po nich skáču nahoru a u toho sbírámě kytky
pygame.init()
  
rozliseni_okna = (1280, 900)
okno = pygame.display.set_mode(rozliseni_okna)
pygame.display.set_caption("idk prostě hra xd")


barva_pozadi = (50, 50, 50)

class Objekty:
    def __init__(self, x_pos, y_pos, x_velikost, y_velikost, rychlost):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velikost = x_velikost
        self.y_velikost = y_velikost
        self.rychlost = rychlost

    def posun(self):
        self.y_pos += self.rychlost

def pad_veci(self):
    random.randint(rozliseni_okna[0] - veci.x_velikost) 


kyselina_textura = pygame.image.load('kyselina.png')
man_textura = pygame.image.load("normal_man.png")
man_textura_skok = pygame.image.load("jumping_man.png")


hrac = Objekty(75, 700, 50, 50, 10)
kyselina = Objekty(900, 600, 50, 50, 4)
veci = Objekty(0, 0, 50, 50, 5)


je_na_zemi = True
rychlost_skok = 20
gravitace = 0.9
rychlost_y = 0


clock = pygame.time.Clock()
fps = 75




while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    stisknute_klavesy = pygame.key.get_pressed()


    if stisknute_klavesy[pygame.K_LEFT]:
        hrac.x_pos -= hrac.rychlost

    if stisknute_klavesy[pygame.K_RIGHT]:
        hrac.x_pos += hrac.rychlost

    if stisknute_klavesy[pygame.K_SPACE] and je_na_zemi:
        je_na_zemi = False
        rychlost_y = -rychlost_skok

    if not je_na_zemi:
        hrac.y_pos += rychlost_y
        rychlost_y += gravitace

        if hrac.y_pos >= 700:
            hrac.y_pos = 700
            je_na_zemi = True
            rychlost_y = 0

    okno.fill(barva_pozadi)


    if hrac.x_pos >= 1280 - hrac.x_velikost:
        hrac.x_pos = 1280 - hrac.x_velikost



    if not je_na_zemi:
        okno.blit(man_textura_skok, (hrac.x_pos, hrac.y_pos))
    else:
        okno.blit(man_textura, (hrac.x_pos, hrac.y_pos))
        
    #okno.blit(kyselina_textura, (kyselina.x_pos, kyselina.y_pos))


    pygame.display.update()


    clock.tick(fps)

