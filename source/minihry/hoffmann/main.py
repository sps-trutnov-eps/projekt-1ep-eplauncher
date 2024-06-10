import pygame
import sys
import random
import time

pygame.init()

rozliseni_okna = (1280, 900)
okno = pygame.display.set_mode(rozliseni_okna)
pygame.display.set_caption("idk prostě hra xd")

barva_pozadi = (50, 50, 50)


class Objekty:
    def __init__(self, x_pos, y_pos, x_velikost, y_velikost, rychlost, barva):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velikost = x_velikost
        self.y_velikost = y_velikost
        self.rychlost = rychlost
        self.barva = barva

    def posun(self):
        self.y_pos += self.rychlost

barva_ctverecku = (255, 255, 255)
padaci_objekty = []

hrac = Objekty(75, 850, 50, 50, 10, (102, 178, 255))
cil = Objekty(0, 0, 1280, 25, 0, (0, 102, 0))

je_na_zemi = True
rychlost_skok = 20
rychlost_skok_2 = 0.00000000000001
gravitace = 0.9
rychlost_y = 0
na_platforme = None

clock = pygame.time.Clock()
fps = 75

last_spawn_time = time.time()
spawn_interval = random.uniform(0.25, 0.75)

def vytvor_novy_objekt():
    x_pos = random.randint(0, rozliseni_okna[0] - 60)
    nova_veci = Objekty(x_pos, 0, 60, 25, 3, barva_ctverecku)
    padaci_objekty.append(nova_veci)

def kontrola_kolizi(hrac, objekt):
    if (hrac.x_pos < objekt.x_pos + objekt.x_velikost and
        hrac.x_pos + hrac.x_velikost > objekt.x_pos and
        hrac.y_pos + hrac.y_velikost > objekt.y_pos and
        hrac.y_pos + hrac.y_velikost < objekt.y_pos + objekt.y_velikost and
        rychlost_y > 0):
        return True
    return False

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
        na_platforme = None
        
    if stisknute_klavesy[pygame.K_LEFT] and je_na_zemi:
        je_na_zemi = False
        rychlost_y = -rychlost_skok_2
        na_platforme = None
        
    if stisknute_klavesy[pygame.K_RIGHT] and je_na_zemi:
        je_na_zemi = False
        rychlost_y = -rychlost_skok_2
        na_platforme = None



    if not je_na_zemi:
        hrac.y_pos += rychlost_y
        rychlost_y += gravitace

        if na_platforme:
            if kontrola_kolizi(hrac, na_platforme):
                hrac.y_pos = na_platforme.y_pos - hrac.y_velikost
                je_na_zemi = True
                rychlost_y = 0
            else:
                na_platforme = None

        for objekt in padaci_objekty:
            if kontrola_kolizi(hrac, objekt):
                hrac.y_pos = objekt.y_pos - hrac.y_velikost
                je_na_zemi = True
                rychlost_y = 0
                na_platforme = objekt
                break

        if hrac.y_pos >= 850:
            hrac.y_pos = 850
            je_na_zemi = True
            rychlost_y = 0
            na_platforme = None

    if na_platforme:
        if hrac.y_pos + hrac.y_velikost < 850:
            hrac.y_pos += na_platforme.rychlost
        else:
            na_platforme = None

    if hrac.x_pos >= 1280 - hrac.x_velikost:
        hrac.x_pos = 1280 - hrac.x_velikost
    if hrac.x_pos <= 0:
        hrac.x_pos = 0

    okno.fill(barva_pozadi)

    current_time = time.time()
    if current_time - last_spawn_time > spawn_interval:
        vytvor_novy_objekt()
        spawn_interval = random.uniform(0.10, 0.5)
        last_spawn_time = current_time

    for objekt in padaci_objekty:
        if objekt.y_pos <= 850:
            objekt.posun()
        else:
            padaci_objekty.remove(objekt)  

    for objekt in padaci_objekty:
        pygame.draw.rect(okno, objekt.barva, (objekt.x_pos, objekt.y_pos, objekt.x_velikost, objekt.y_velikost))

    pygame.draw.rect(okno, hrac.barva, (hrac.x_pos, hrac.y_pos, hrac.x_velikost, hrac.y_velikost))
    pygame.draw.rect(okno, cil.barva, (cil.x_pos, cil.y_pos, cil.x_velikost, cil.y_velikost))
    
    pygame.display.update()
    clock.tick(fps)

