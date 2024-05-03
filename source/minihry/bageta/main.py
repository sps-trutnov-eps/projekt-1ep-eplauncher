import random
import sys
import pygame
pygame.init()

okno = pygame.display.set_mode((1400, 800))
obrazek_automat = pygame.image.load("automat.png")
obrazek_automat_vklad = pygame.image.load("automat_vklad.png")
obrazek_10_korun = pygame.image.load("10_korun.png")
obrazek_zed = pygame.image.load("zeď.png")



def automat():
    while True:
        click_mysi = 0
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()

                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_mysi = event.button
                
 
                
                
        kurzor_x, kurzor_y = pygame.mouse.get_pos()       
        #print(kurzor_x, kurzor_y)
        
        if kurzor_x > 840 and kurzor_x < 932 and kurzor_y > 360 and kurzor_y < 480 and click_mysi == 1:
            print("zadání kódu")
            
            
        if kurzor_x > 872 and kurzor_x < 930 and kurzor_y > 491 and kurzor_y < 557 and click_mysi == 1:
            print("vložení mince")            
            
        if kurzor_x > 900 and kurzor_x < 932 and kurzor_y > 318 and kurzor_y < 351 and click_mysi == 1:
            print("nemáš kartu")         
        
        
        
        
        
        
        okno.blit(obrazek_zed, (0,0))
        okno.blit(obrazek_automat, (450,100))
        pygame.display.flip()
        
automat()
