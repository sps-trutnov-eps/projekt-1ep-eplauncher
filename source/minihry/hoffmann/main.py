import pygame
import sys

pygame.init()

rozliseni_okna = (1280, 900)
okno = pygame.display.set_mode(rozliseni_okna)

class Objekty:
    def __init__(self, x_pos, y_pos, x_velikost, y_velikost, rychlost):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_velikost = x_velikost
        self.y_velikost = y_velikost
        self.rychlost = rychlost
        
    def posun(self):
        self.y_pos += self.rychlost

hrac = Objekty (1200, 850, 50, 50, 5)
koule = Objekty (1000, 500, 50, 50, 4)


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
         
        

    okno.fill((50, 50, 50))
    
    
    pygame.draw.rect(okno, (255, 255, 255), (hrac.x_pos, hrac.y_pos, hrac.x_velikost, hrac.y_velikost))
    pygame.draw.rect(okno, (100, 255, 0), (koule.x_pos, koule.y_pos, koule.x_velikost, koule.y_velikost))
    
    pygame.display.update()
