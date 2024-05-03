import random
import sys
import pygame
pygame.init()

okno = pygame.display.set_mode((1400, 800))
obrazek_automat = pygame.image.load("automat.png")
obrazek_automat_vklad = pygame.image.load("automat_vklad.png")
obrazek_10_korun = pygame.image.load("10_korun.png")




while True:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()    
    
    
    
    
    
    
    
    
    
    okno.fill((40,100,200))
    okno.blit(obrazek_automat_vklad, (0,0))
    okno.blit(obrazek_10_korun, (774,150))
    pygame.display.flip()
    
