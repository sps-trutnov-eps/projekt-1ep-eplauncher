import random
import sys
import pygame
pygame.init()
clock = pygame.time.Clock()

okno = pygame.display.set_mode((1400, 800))
obrazek_automat = pygame.image.load("minihry/bageta/automat.png")
obrazek_automat_vklad = pygame.image.load("minihry/bageta/automat_vklad.png")
obrazek_10_korun = pygame.image.load("minihry/bageta/10_korun.png")
obrazek_zed = pygame.image.load("minihry/bageta/zeď.png")
obrazek_display = pygame.image.load("minihry/bageta/displej.png")



l_sipka_plna = pygame.image.load("minihry/bageta/l_sipka_plna.png")
p_sipka_plna = pygame.image.load("minihry/bageta/p_sipka_plna.png")
d_sipka_plna = pygame.image.load("minihry/bageta/d_sipka_plna.png")
n_sipka_plna = pygame.image.load("minihry/bageta/n_sipka_plna.png")

l_sipka_prazdna = pygame.image.load("minihry/bageta/l_sipka_prazdna.png")
p_sipka_prazdna = pygame.image.load("minihry/bageta/p_sipka_prazdna.png")
d_sipka_prazdna = pygame.image.load("minihry/bageta/d_sipka_prazdna.png")
n_sipka_prazdna = pygame.image.load("minihry/bageta/n_sipka_prazdna.png")

obrazek_bageta_1 = pygame.image.load("minihry/bageta/bageta_1.png")
obrazek_bageta_2 = pygame.image.load("minihry/bageta/bageta_2.png")
obrazek_bageta_3 = pygame.image.load("minihry/bageta/bageta_3.png")



splneno = False 

penezenka = 7

vlozeno = 0

font = pygame.font.Font(None, 50)
tier_1 = False 
tier_2 = False 
tier_3 = False


game_running = False
function_running = False
thingy_running = False
prohra_going_on = False
font = pygame.font.Font(None, 50)

def automat():
    global splneno, penezenka, vlozeno, font, tier_1, tier_2, tier_3
    
    splneno = False 

    penezenka = 7

    vlozeno = 0

    tier_1 = False 
    tier_2 = False 
    tier_3 = False

   
    
    global okno, prohra_going_on, thingy_running, game_running, function_running
    okno = pygame.display.set_mode((1400, 800))
    
    game_running = False
    function_running = False
    thingy_running = False
    prohra_going_on = False 
    
    game_running = True
    while game_running:
        if penezenka == 0:
            if vlozeno < 2:
                #print("konec")
                prohra()
                
        click_mysi = 0
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_running = False
                prohra_going_on = False
                thingy_running = False
                game_running = False
                function_running = False


                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_mysi = event.button
                
 
                
                
        kurzor_x, kurzor_y = pygame.mouse.get_pos()       
        #print(kurzor_x, kurzor_y)
        
        if kurzor_x > 840 and kurzor_x < 932 and kurzor_y > 360 and kurzor_y < 480 and click_mysi == 1:
            if vlozeno >= 2:
                if splneno == False:
                    kod()

            
        if kurzor_x > 872 and kurzor_x < 930 and kurzor_y > 491 and kurzor_y < 557 and click_mysi == 1:
            vklad_mince()


            
        if splneno == True:
         if vlozeno >= 2 and vlozeno < 5:
            #print("ziskal jsi bagetu")
            okno.blit(obrazek_bageta_1, (450, 20))
            tier_1 = True
            
        if splneno == True:
         if vlozeno >= 5 and vlozeno < 7:
            #print("ziskal jsi bagetu standart")
            okno.blit(obrazek_bageta_2, (450, 20))
            tier_2 = True
            
        if splneno == True:
         if vlozeno == 7:
            #print("ziskal jsi bagetu deluxe")
            okno.blit(obrazek_bageta_3, (450, 20))
            tier_3 = True                



        okno.blit(obrazek_zed, (0,0))
        okno.blit(obrazek_automat, (450,100))
        pygame.display.flip()
        if tier_1 == True :
            return "normalni_bageta"
        if tier_2 == True :
            return "bageta_standart"
        if tier_3 == True :
            return "bageta_deluxe"

    okno = pygame.display.set_mode((800, 800))
            
        

        
        
def vklad_mince():
    global font, penezenka, vlozeno, okno, prohra_going_on, thingy_running, game_running, function_running

    
    
    space_cooldown = 0
    x_mince = 402
    plus = True
    minus = False 
    function_running = True
    while function_running:
        
         for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                function_running = False
                prohra_going_on = False
                thingy_running = False
                game_running = False
                function_running = False
                
         if x_mince <= 373:
             minus = False
             plus = True
             
         if x_mince >= 1246:
             minus = True
             plus = False            

         if minus:
             if vlozeno == 0:
                 x_mince -= random.randint(20,35)
             if vlozeno == 1:
                 x_mince -= random.randint(22,37)
             if vlozeno == 2:
                 x_mince -= random.randint(24,40)
             if vlozeno > 2:
                 x_mince -= random.randint(28,45)
                 
         if plus:
             if vlozeno == 0:
                 x_mince += random.randint(20,35)
             if vlozeno == 1:
                 x_mince += random.randint(22,37)
             if vlozeno == 2:
                 x_mince += random.randint(24,40)
             if vlozeno > 2:
                 x_mince += random.randint(28,45)
             
         space_cooldown -= 1
         space = False
         if penezenka > 0:
             if pygame.key.get_pressed()[pygame.K_SPACE]:
                if space_cooldown < 0:
                    space = True
                    space_cooldown = 20


         if pygame.key.get_pressed()[pygame.K_ESCAPE]:
             return 
             
             
             

             
             
             
         Trefa = False
         Vedle = False 
         if x_mince >= 695 and x_mince <= 850 and space:
             penezenka -= 1
             #print(penezenka)
             #print("trefa")
             Trefa = True
             vlozeno += 1
             
         if x_mince < 695 and space:
             penezenka -= 1
             #print(penezenka)
             #print("vedle")
             Vedle = True 
         if x_mince > 850 and space:
             penezenka -= 1
             #print(penezenka)
             #print("vedle")
             Vedle = True
             
         penezenka_status = font.render('Peněženka: ' + str(penezenka*10) + "Kč", True, (255, 255, 255))    
                
         okno.blit(obrazek_automat_vklad, (0,0))
         okno.blit(obrazek_10_korun, (x_mince,150))
         okno.blit(penezenka_status, (2, 5))
         okno.blit(font.render("Vloženo: "+ str(vlozeno*10)+"Kč", True, (255, 255, 255)), (700, 700))
         okno.blit(pygame.font.Font(None, 30).render("Vlož minci stisknutím SPACE", True, (103, 103, 103)), (350, 700))
         if Trefa:
             okno.fill((0,150,0))
         if Vedle:
             okno.fill((150,0,0))
         pygame.display.flip()
         clock.tick(60)       





def kod():
    global font
    global penezenka
    global vlozeno
    global okno
    timer = 180
    
    arrow_images = {
    "up": pygame.image.load("minihry/bageta/n_sipka_prazdna.png"),
    "down": pygame.image.load("minihry/bageta/d_sipka_prazdna.png"),
    "left": pygame.image.load("minihry/bageta/l_sipka_prazdna.png"),
    "right": pygame.image.load("minihry/bageta/p_sipka_prazdna.png")
    }
    
    arrow_correct_images = {
    "up": pygame.image.load("minihry/bageta/n_sipka_plna.png"),
    "down": pygame.image.load("minihry/bageta/d_sipka_plna.png"),
    "left": pygame.image.load("minihry/bageta/l_sipka_plna.png"),
    "right": pygame.image.load("minihry/bageta/p_sipka_plna.png")
    }
    
    arrow_positions = [(113, 100), (295, 100), (480, 100), (665, 100), (850, 100), (1035, 100)]
    
    arrow_sequence = [random.choice(["up", "down", "left", "right"]) for _ in range(6)]
    current_index = 0
    global splneno, prohra_going_on, thingy_running, game_running, function_running
    splneno = False
    thingy_running = True
    while thingy_running:
        okno.blit(obrazek_display, (0,0))
        if current_index == len(arrow_sequence):
            if timer >= 0:
                splneno = True
        if timer == -1:
            if splneno == False:
                prohra()
                thingy_running = False

        
        if timer > -1:
            timer -= 1
            #print(timer)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                thingy_running = False
                prohra_going_on = False
                thingy_running = False
                game_running = False
                function_running = False
                okno = pygame.display.set_mode((800, 800))

            elif event.type == pygame.KEYDOWN:
                if current_index < len(arrow_sequence):
                    if (event.key == pygame.K_UP and arrow_sequence[current_index] == "up") or \
                       (event.key == pygame.K_DOWN and arrow_sequence[current_index] == "down") or \
                       (event.key == pygame.K_LEFT and arrow_sequence[current_index] == "left") or \
                       (event.key == pygame.K_RIGHT and arrow_sequence[current_index] == "right"):
                        current_index += 1    
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
             return

        for i, direction in enumerate(arrow_sequence):
         if i < current_index:
            okno.blit(arrow_correct_images[direction], arrow_positions[i])
         else:
            okno.blit(arrow_images[direction], arrow_positions[i])             
                    
                    
        if splneno:
           #print("SKVĚLE!")
           penezenka = 0
                    
        
        okno.blit(font.render(str(round(timer/60)), True, (255, 255, 255)), (700, 700))

               

                
                


        pygame.display.flip()
        clock.tick(60)
        
def prohra():
    global font, okno, prohra_going_on, thingy_running, game_running, function_running
    prohra_going_on = True
    while prohra_going_on:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                prohra_going_on = False
                thingy_running = False
                game_running = False
                function_running = False
        
        
        okno.fill((255,0,0))
        okno.blit(font.render("prohrál jsi", True, (255,255,255)), (700, 200))
        pygame.display.flip()
    okno = pygame.display.set_mode((800, 800))


if __name__ == "__main__":
    automat()
