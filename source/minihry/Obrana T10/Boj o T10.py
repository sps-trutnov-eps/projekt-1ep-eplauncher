import sys
import pygame
pygame.init()

rozliseni_okna = (1320, 768)
okno = pygame.display.set_mode(rozliseni_okna)
#----------------------------------------------------------------------
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      
    okno.fill(143, 64, 32)
      
#----------------------------------------------------------------------
            
            
            
            
            
    pygame.display.flip()