# Flappy Bird
import sys
import pygame
import random
def display_score():
    time = int(pygame.time.get_ticks()/1000) - start_time
    score = font.render(f'{time}',False, (64, 64, 64))
    score_rect = score.get_rect(center = (400, 50))
    okno.blit(score, score_rect)
    return time





pygame.init()
pygame.display.set_caption('minihry/Flappy bird/Flappy Bird')
rozliseni_okna = (800, 600)
okno = pygame.display.set_mode(rozliseni_okna)
tlacitka = pygame.key.get_pressed()
game_active = False   
start_time = 0
score_text = 0 
font = pygame.font.Font(None, 50)
font_1 = pygame.font.Font(None, 100)
clock = pygame.time.Clock()
fps = 60
pipe_gap = 250
pipe_frequency = 2500
last_pipe = pygame.time.get_ticks()
# pozadí
mesto = pygame.image.load('minihry/Flappy bird/1.pozadí FP.jpg').convert()
hlina = pygame.image.load('minihry/Flappy bird/1.5 pozadí FP.jpg').convert()
mesto_2 = pygame.image.load('minihry/Flappy bird/pozadí 2 .png').convert()
hlina_2 = pygame.image.load('minihry/Flappy bird/pozadí 2.5.png').convert()
mesto_3 = pygame.image.load('minihry/Flappy bird/pozadi 3.png').convert()
hlina_3 = pygame.image.load('minihry/Flappy bird/pozadi 3.5 .png').convert()
# parametry pozadí
rychlost_hliny = 3
pozice_hliny = 0
rychlost_mesta = 1
pozice_mesta = 0
rychlost_hliny_2 = 3
pozice_hliny_2 = 0
rychlost_mesta_2 = 1
pozice_mesta_2 = 0
rychlost_hliny_3 = 3
pozice_hliny_3 = 0
rychlost_mesta_3 = 1
pozice_mesta_3 = 0
# PTÁK
pozice_ptaka_x = 150
pozice_ptaka_y = 300
pozice_ptaka_red_x = 150
pozice_ptaka_red_y = 300
pozice_ptaka_blue_x = 150
pozice_ptaka_blue_y = 300
class Ptak(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('minihry/Flappy bird/zluty_ptak - kopie.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.gravitace = 0
        
        
    def update(self):
        # gravitace
        if game_active == True:
            self.gravitace += 1/4
            if self.gravitace > 8:
                self.score_text = self.gravitace = 8
            self.rect.y += self.gravitace
        
        # skoky
        tlacitka = pygame.key.get_pressed()
        if tlacitka[pygame.K_SPACE]:
            self.gravitace = - 5
        
             
            
            
        
        
ptak_group = pygame.sprite.Group()
ptak = Ptak(pozice_ptaka_x, pozice_ptaka_y)
ptak_group.add(ptak)
# Skiny
ptak_red = pygame.image.load('minihry/Flappy bird/cerveny_ptak.png').convert_alpha()
ptak_red_rect = ptak_red.get_rect(center = (400, 300))
ptak_red = pygame.transform.rotozoom(ptak_red, 0, 3)
ptak_blue = pygame.image.load('minihry/Flappy bird/modry_ptak.png').convert_alpha()
ptak_blue_rect = ptak_blue.get_rect(center = (400, 300))
ptak_blue = pygame.transform.rotozoom(ptak_blue, 0, 3)
zluta = True 
cervena = False  
modra = False
# cerveny ptak
class Ptak_red(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('minihry/Flappy bird/cerveny_ptak.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.gravitace = 0
        
        
    def update(self):
        # gravitace
        if game_active == True:
            self.gravitace += 1/4
            if self.gravitace > 8:
                self.gravitace = 8
            self.rect.y += self.gravitace
        
        #skoky
        tlacitka = pygame.key.get_pressed()
        if tlacitka[pygame.K_SPACE]:
            self.gravitace = - 5
            
ptakred_group = pygame.sprite.Group()
ptakred_skin = Ptak_red(pozice_ptaka_red_x, pozice_ptaka_red_y)
ptakred_group.add(ptakred_skin)
# modry ptak
class Ptak_blue(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('minihry/Flappy bird/modry_ptak.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.gravitace = 0
        
    def update(self):
        # gravitace
        self.gravitace += 1/4
        if self.gravitace > 8:
            self.gravitace = 8
        self.rect.y += self.gravitace
        
        #skoky
        tlacitka = pygame.key.get_pressed()
        if tlacitka[pygame.K_SPACE]:
            self.gravitace = -5
            
ptakblue_group = pygame.sprite.Group()
ptakblue_skin = Ptak_blue(pozice_ptaka_blue_x, pozice_ptaka_blue_y)
ptakblue_group.add(ptakblue_skin)
# Intro
ptak_intro = pygame.image.load('minihry/Flappy bird/zluty_ptak - kopie.png').convert_alpha()
ptak_intro =pygame.transform.rotozoom(ptak_intro, 0, 3) 
ptak_intro_rect = ptak_intro.get_rect(center = (400, 300))
text = font_1.render('Press space to fly', False , (255, 255, 255))
text_rect = text.get_rect(center = (400, 400))
text_bird = font_1.render('Flappy Bird', False, (0, 0, 255))
text_bird_rect = text_bird.get_rect(center = (400, 100))
skin_text = font.render('Chosse a skin q,w,e', False, (0, 0, 0))
skin_text_rect = skin_text.get_rect(center = (200, 200))
#Trubky
rychlost_trubky = 3
class pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, smer):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('minihry/Flappy bird/trubka.png')
        self.image = pygame.image.load('minihry/Flappy bird/trubka.png')
        self.rect = self.image.get_rect()
        if smer == 1:
            self.image = pygame.transform.flip(self.image, False, True )
            self.rect.bottomleft = [x, y-int(pipe_gap / 2)]
        if smer == -1:
            self.rect.topleft = [x, y+int(pipe_gap / 2)]
            
    def update(self):
        self.rect.x -= rychlost_trubky
        if self.rect.right < -200:
            self.kill()
        
        
pipe_group = pygame.sprite.Group()
# reset
def reset_game():
    pipe_group.empty()
    ptak.rect.x = pozice_ptaka_x
    ptak.rect.y = pozice_ptaka_y
    ptakred_skin.rect.x = pozice_ptaka_red_x
    ptakred_skin.rect.y = pozice_ptaka_red_y
    ptakblue_skin.rect.x = pozice_ptaka_blue_x
    ptakblue_skin.rect.y = pozice_ptaka_blue_y



def main():
    global game_active, last_pipe, pipe_frequency, rychlost_trubky, zluta, score_text, cervena, modra, tlacitka, pozice_hliny,pozice_mesta, start_time, pozice_hliny_2, pozice_hliny_3, rychlost_hliny_2, rychlost_hliny_3, pozice_mesta_2, rychlost_mesta_2, pozice_mesta_3, rychlost_mesta_3
    game_is_running = True
    while game_is_running:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                game_is_running = False
                    
        #kolize
        # zluty
        if game_active == True:
            if pygame.sprite.groupcollide(ptak_group, pipe_group, False , False) or ptak.rect.top < 0 or ptak.rect.bottom > 600:
                game_active = False
        # cerveny
            if pygame.sprite.groupcollide(ptakred_group, pipe_group, False , False) or ptakred_skin.rect.top < 0 or ptakred_skin.rect.bottom > 600:
                game_active = False
        # modry
            if pygame.sprite.groupcollide(ptakblue_group, pipe_group, False , False) or ptakblue_skin.rect.top < 0 or ptakblue_skin.rect.bottom > 600:
                game_active = False 
        # Pozadí   
        if game_active == True:
            okno.blit(mesto, (pozice_mesta, 0))
            okno.blit(hlina, (pozice_hliny, 528))
            pozice_hliny -= rychlost_hliny
            pozice_mesta -= rychlost_mesta
            clock.tick(fps)
            score_text = display_score()
            if abs(pozice_hliny) > 30:
                pozice_hliny = 0
            if abs(pozice_mesta) > 60:
                pozice_mesta = 0
                    
            if game_active == True and score_text > 30 and score_text < 60:
                okno.blit(mesto_2, (pozice_mesta_2, 0))
                okno.blit(hlina_2, (pozice_hliny_2, 528))
                pozice_hliny_2 -= rychlost_hliny_2
                pozice_mesta_2 -= rychlost_mesta_2
                score_text = display_score()
                if abs(pozice_hliny_2) > 30:
                    pozice_hliny_2 = 0
                if abs(pozice_mesta_2) > 60:
                    pozice_mesta_2 = 0  
                pipe_gap = 200
                pipe_frequency = 2000
                    
            if game_active == True and score_text > 59:
                okno.blit(mesto_3, (pozice_mesta_3, 0))
                okno.blit(hlina_3, (pozice_hliny_3, 528))
                pozice_hliny_3 -= rychlost_hliny_3
                pozice_mesta_3 -= rychlost_mesta_3
                score_text = display_score()
                if abs(pozice_hliny_3) > 30:
                    pozice_hliny_3 = 0
                if abs(pozice_mesta_3) > 50:
                    pozice_mesta_3 = 0  
                pipe_gap = 150
                pipe_frequency = 1500
                
                
        # Trubky
        if game_active == True:
            pipe_group.draw(okno)
            pipe_group.update()
        
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            dolni_pipe = pipe(800, 300 + pipe_height, -1)
            horni_pipe = pipe(800, 300 + pipe_height, 1)
            pipe_group.add(dolni_pipe) 
            pipe_group.add(horni_pipe)
            last_pipe = time_now

        if game_active == True:
            rychlost_trubky += 1/500

        # Intro
        if game_active == False:
            okno.fill((94, 129, 162))
            if zluta == True:
                okno.blit(ptak_intro, ptak_intro_rect)
            okno.blit(text_bird, text_bird_rect)
            okno.blit(skin_text, skin_text_rect)
            tlacitka = pygame.key.get_pressed()
            score_message = font_1.render(f'Your score: {score_text}', False, (255, 255, 255))
            score_message_rect = score_message.get_rect(center = (400, 400))
            if score_text == 0:
                okno.blit(text, text_rect)
            else:
                okno.blit(score_message, score_message_rect)
            if tlacitka[pygame.K_SPACE]:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)   
                rychlost_trubky = 3
                pipe_frequency = 2500
                pipe_gap = 250
                reset_game()        


        if game_active == False:
            if tlacitka[pygame.K_w]:
                zluta = False
                cervena = True
                modra = False  
            if cervena == True:
                okno.blit(ptak_red, ptak_red_rect)
                
                
            if tlacitka[pygame.K_e]:
                cervena = False
                modra = True
                zluta = False
            if modra == True:
                okno.blit(ptak_blue,ptak_blue_rect)
            
            if tlacitka[pygame.K_q]:
                modra = False
                zluta = True 
                cervena = False
                
        if game_active == True:
            # cerveny
            if cervena == True:
                ptakred_group.draw(okno)
                ptakred_group.update()
            # zluty   
            if zluta == True:  
                ptak_group.draw(okno)   
                ptak_group.update()
            # modry
            if modra == True :
                ptakblue_group.draw(okno)
                ptakblue_group.update()




        pygame.display.update()


if __name__ == '__main__':
    main()
