
import time
import pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()
fps = 60
clock = pygame.time.Clock()

Wave1 = False
wave2 = False
wave3 = False
vel_enm = 0
vel_cooldown = 0
rozliseni_okna = (1200, 800)
dash_rych = 22
okno = pygame.display.set_mode(rozliseni_okna)
dash = False
start_time = 0
cooldown = False
shoot = False
vel_hrc = 50
class hrac(object):
    def __init__(self, hp, spd,x , y,):
        self.hp = hp
        self.spd = spd
        self.x = x
        self.y = y

       
        
    def draw(self):
        pygame.draw.rect(okno,(0,0,0),(self.x,self.y,vel_hrc,vel_hrc))
        
    
    
    
hrc = hrac(100, 5.5, 600, 400,)




class predmety:
    def __init__(self, dmg, hp, spd,):
        self.hp = hp
        self.dmg = dmg
        self.hp = hp
        self.spd = spd
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
        self.colour = colour


    def draw(self):
         pygame.draw.circle(okno,(self.colour),(self.x,self.y),vel_enm)



ez = enemy(20,10,3,10,10,(0,250,0))
mid = enemy(50,12,5, 250, 10,(255,95,21))
hard = enemy(100,100,9,500,10,(255,0,0))



run = True




while run:
    okno.fill((0, 90, 70))
    
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
    if hrc.hp == 0:
        vel_hrc = 0
        print("prohral jis")
    if hard.x == hrc.x and hard.y == hrc.y:
        hrc.hp -= hard.dmg
    
      
    if stisknute_klavesy[pygame.K_SPACE]:
        Wave1 = True 
    
    if stisknute_klavesy[pygame.K_LSHIFT] and vel_cooldown < 1:
        dash = True
        start_time = time.perf_counter()
        cooldown = True
        vel_cooldown = 150
    if cooldown:
        vel_cooldown -= 3
        
        



    if Wave1:
        vel_enm = 50
        
        
    if vel_enm == 50:
        if hrc.x > ez.x:
            ez.x = ez.x + ez.spd        
        if hrc.x < ez.x:
            ez.x = ez.x - ez.spd
        if hrc.y > ez.y:
            ez.y = ez.y + ez.spd
        if hrc.y < ez.y:
            ez.y = ez.y - ez.spd    
    if vel_enm == 50:
        if hrc.x > mid.x:
            mid.x = mid.x + mid.spd        
        if hrc.x < mid.x:
            mid.x = mid.x - mid.spd
        if hrc.y > mid.y:
            mid.y = mid.y + mid.spd
        if hrc.y < mid.y:
            mid.y = mid.y - mid.spd 
    if vel_enm == 50:
        if hrc.x > hard.x:
            hard.x = hard.x + hard.spd        
        if hrc.x < hard.x:
            hard.x = hard.x - hard.spd
        if hrc.y > hard.y:
            hard.y = hard.y + hard.spd
        if hrc.y < hard.y:
            hard.y = hard.y - hard.spd        
    if dash:
        hrc.spd = dash_rych

    if dash and time.perf_counter() - start_time > 0.1:
        dash = False
        hrc.spd = 5.5

        
    
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
    ez.draw()
    mid.draw()
    hard.draw()
    pygame.draw.rect(okno, (0, 0, 0), (25, 750, vel_cooldown, 30)) #cooldown bar
    pygame.display.update()

