import random
import sys
import pygame
pygame.init()
clock = pygame.time.Clock()

okno = pygame.display.set_mode((1400, 800))
obrazek_automat = pygame.image.load("automat.png")
obrazek_automat_vklad = pygame.image.load("automat_vklad.png")
obrazek_10_korun = pygame.image.load("10_korun.png")
obrazek_zed = pygame.image.load("zeď.png")


global penezenka
penezenka = 5
global font
font = pygame.font.Font(None, 50) 


def automat():
    global font
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
            vklad_mince()           
            
        if kurzor_x > 900 and kurzor_x < 932 and kurzor_y > 318 and kurzor_y < 351 and click_mysi == 1:
            print("nemáš kartu")
            
        if kurzor_x > 521 and kurzor_x < 797 and kurzor_y > 642 and kurzor_y < 737 and click_mysi == 1:
            print("nic zatím nevypdalo")              
        
        
        
        

        okno.blit(obrazek_zed, (0,0))
        okno.blit(obrazek_automat, (450,100))
        pygame.display.flip()
        
        
        
def vklad_mince():
    global font
    global penezenka
    

    
    
    space_cooldown = 0
    x_mince = 402
    plus = True
    minus = False 
    while True:
        
         for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()
                
         if x_mince <= 373:
             minus = False
             plus = True
             
         if x_mince >= 1246:
             minus = True
             plus = False            

         if minus:
             x_mince -= random.randint(17,30)
         if plus:
             x_mince += random.randint(17,30)
             
         space_cooldown -= 1
         space = False
         if penezenka > 0:
             if pygame.key.get_pressed()[pygame.K_SPACE]:
                if space_cooldown < 0:
                    space = True
                    space_cooldown = 30


             
             
             
             

             
             
             
         Trefa = False
         Vedle = False 
         if x_mince >= 695 and x_mince <= 850 and space:
             penezenka -= 1
             print(penezenka)
             print("trefa")
             Trefa = True 
             
         if x_mince < 695 and space:
             penezenka -= 1
             print(penezenka)
             print("vedle")
             Vedle = True 
         if x_mince > 850 and space:
             penezenka -= 1
             print(penezenka)
             print("vedle")             
             Vedle = True
             
         penezenka_status = font.render('Peněženka: ' + str(penezenka*10) + "Kč", True, (255, 255, 255))    
                
         okno.blit(obrazek_automat_vklad, (0,0))
         okno.blit(obrazek_10_korun, (x_mince,150))
         okno.blit(penezenka_status, (2, 5))
         okno.blit(pygame.font.Font(None, 30).render("Vlož minci stisknutím SPACE", True, (103, 103, 103)), (350, 700))
         if Trefa:
             okno.fill((0,150,0))
         if Vedle:
             okno.fill((150,0,0))
         pygame.display.flip()
         clock.tick(60)       
                



automat()
