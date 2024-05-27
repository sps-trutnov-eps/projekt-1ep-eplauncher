
import time
import pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()
fps = 60
clock = pygame.time.Clock()


vel_enm = 0
vel_cooldown = 0
rozliseni_okna = (1200, 800)
okno = pygame.display.set_mode(rozliseni_okna)
dash = False
start_time = 0
cooldown = False
shoot = False
vel_hrc = 50
#class boss(pygame.sprite.Sprite):
 #   def __init__(self, hp, spd, x, y):
  #      self.hp = hp
   #     self.spd = spd
    #    self.x = x
     #   self.y = y
      #  pygame.sprite.Sprite.__init__(self)
       # self.image = pygame.image.load('images/M_tank.png')
#       self.images.append(img)
        # self.image = self.images[0]
        #self.rect = self.image.get_rect()
        
#Mar = boss(500,5,150,50)    
        

class hrac(object):
    def __init__(self, hp, spd,x , y,):
        self.hp = hp
        self.spd = spd
        self.x = x
        self.y = y

       
        
    def draw(self):
        pygame.draw.rect(okno,(0,0,0),(self.x,self.y,vel_hrc,vel_hrc))
        
    
    
    
hrc = hrac(100, 5.5, 600, 400,)

load = pygame.image.load("images\M_tank.png")


class Bullet(object):
    def __init__(self, x, y, mouse_x, mouse_y,):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.lifetime = 50
        self.speed = 30
        self.angle = math.atan2(mouse_y-self.y, mouse_x-self.x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

        
    def draw(self, draw):
        self.x += int(self.x_vel)
        self.y += int(self.y_vel)

        pygame.draw.circle(okno, (255, 255, 255), (self.x, self.y), 5)
        self.lifetime-= 1
bullets = []    
        
red = (250,0,0)
green = (0,250,0)
orange = (255,130,13)

class enemy(object):
    def __init__(self, hp, dmg , spd, x, y,colour):
        self.hp = hp
        self.dmg = dmg
        self.spd = spd
        self.x = x
        self.y = y



    def draw(self):
         pygame.draw.circle(okno,(self.colour),(self.x,self.y),vel_enm)
run = True
while run:
    okno.fill((128, 70, 27))
    
    x, y = pygame.mouse.get_pos()
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            quit()
            run = False
    if udalost.type == pygame.MOUSEBUTTONDOWN:
        if udalost.button == 1:
            bullets.append(Bullet(hrc.x, hrc. y, x, y))
                 
                 
    stisknute_klavesy = pygame.key.get_pressed()

    

        
    
    if stisknute_klavesy [pygame.K_d]:
        hrc.x += hrc.spd
    if stisknute_klavesy [pygame.K_a]:
        hrc.x -= hrc.spd
    
    if stisknute_klavesy [pygame.K_s] :
        hrc.y += hrc.spd
    if stisknute_klavesy [pygame.K_w]:
        hrc.y -= hrc.spd


    for bullet in bullets:
        if bullet.lifetime <= 0:
            bullets.pop(bullets.index(bullet))
        bullet.draw(okno)
    hrc.draw()   
    clock.tick(fps)
    okno.blit(load,(0,0))
    pygame.display.update()

