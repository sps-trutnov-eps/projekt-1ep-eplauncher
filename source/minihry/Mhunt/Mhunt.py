
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

import pygame
import random
import math
from pygame import mixer

# initializing pygame
pygame.init()

# creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,
								screen_height))

# caption and icon
pygame.display.set_caption("Welcome to Space\
Invaders Game by:- styles")


# Score
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
	score = font.render("Points: " + str(score_val),
						True, (255,255,255))
	screen.blit(score, (x , y ))

def game_over():
	game_over_text = game_over_font.render("GAME OVER",
										True, (255,255,255))
	screen.blit(game_over_text, (190, 250))

# Background Sound
mixer.music.load('data/background.wav')
mixer.music.play(-1)

# player
playerImage = pygame.image.load('data/spaceship.png')
player_X = 370
player_Y = 523
player_Xchange = 0

# Invader
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

for num in range(no_of_invaders):
	invaderImage.append(pygame.image.load('data/alien.png'))
	invader_X.append(random.randint(64, 737))
	invader_Y.append(random.randint(30, 180))
	invader_Xchange.append(1.2)
	invader_Ychange.append(50)

# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage = pygame.image.load('data/bullet.png')
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"

# Collision Concept
def isCollision(x1, x2, y1, y2):
	distance = math.sqrt((math.pow(x1 - x2,2)) +
						(math.pow(y1 - y2,2)))
	if distance <= 50:
		return True
	else:
		return False

def player(x, y):
	screen.blit(playerImage, (x - 16, y + 10))

def invader(x, y, i):
	screen.blit(invaderImage[i], (x, y))

def bullet(x, y):
	global bullet_state
	screen.blit(bulletImage, (x, y))
	bullet_state = "fire"

# game loop
running = True
while running:

	# RGB
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# Controlling the player movement
		# from the arrow keys
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_Xchange = -1.7
			if event.key == pygame.K_RIGHT:
				player_Xchange = 1.7
			if event.key == pygame.K_SPACE:
			
				# Fixing the change of direction of bullet
				if bullet_state is "rest":
					bullet_X = player_X
					bullet(bullet_X, bullet_Y)
					bullet_sound = mixer.Sound('data/bullet.wav')
					bullet_sound.play()
		if event.type == pygame.KEYUP:
			player_Xchange = 0

	# adding the change in the player position
	player_X += player_Xchange
	for i in range(no_of_invaders):
		invader_X[i] += invader_Xchange[i]

	# bullet movement
	if bullet_Y <= 0:
		bullet_Y = 600
		bullet_state = "rest"
	if bullet_state is "fire":
		bullet(bullet_X, bullet_Y)
		bullet_Y -= bullet_Ychange

	# movement of the invader
	for i in range(no_of_invaders):
		
		if invader_Y[i] >= 450:
			if abs(player_X-invader_X[i]) < 80:
				for j in range(no_of_invaders):
					invader_Y[j] = 2000
					explosion_sound = mixer.Sound('data/explosion.wav')
					explosion_sound.play()
				game_over()
				break

		if invader_X[i] >= 735 or invader_X[i] <= 0:
			invader_Xchange[i] *= -1
			invader_Y[i] += invader_Ychange[i]
		# Collision
		collision = isCollision(bullet_X, invader_X[i],
								bullet_Y, invader_Y[i])
		if collision:
			score_val += 1
			bullet_Y = 600
			bullet_state = "rest"
			invader_X[i] = random.randint(64, 736)
			invader_Y[i] = random.randint(30, 200)
			invader_Xchange[i] *= -1

		invader(invader_X[i], invader_Y[i], i)


	# restricting the spaceship so that
	# it doesn't go out of screen
	if player_X <= 16:
		player_X = 16;
	elif player_X >= 750:
		player_X = 750


	player(player_X, player_Y)
	show_score(scoreX, scoreY)
	pygame.display.update()
