import sys
import pygame
import random
import math
from pygame import mixer
#pro nepovoláné čtenáře: GET OUT OF MY SWAMP

pygame.init()


screen_width = 1200
screen_height = 800
okno = pygame.display.set_mode((screen_width,
                                screen_height))


pygame.display.set_caption("Vítej na bojišti\
Mhunt od: Denis")

class pozadi(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
Pozadi = pozadi("images\pozadi.png", [0,0])


score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)


game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
	score = font.render("Points: " + str(score_val),
						True, (0,0,0))
	okno.blit(score, (x , y ))

def game_over():
	game_over_text = game_over_font.render("GAME OVER",
										True, (0,0,0))
	okno.blit(game_over_text, (190, 250))




mixer.music.load('images\pozadi_hudba.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.2)

playerImage = pygame.image.load('images\hrac.png')
player_X = 370
player_Y = 650
player_Xchange = 0


invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

for num in range(no_of_invaders):
	invaderImage.append(pygame.image.load('images\M_tank.png'))
	invader_X.append(random.randint(64, 737))
	invader_Y.append(random.randint(30, 180))
	invader_Xchange.append(1.5)
	invader_Ychange.append(50)


bulletImage = pygame.image.load('images\strela.png')
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 9
bullet_state = "rest"


def isCollision(x1, x2, y1, y2):
	distance = math.sqrt((math.pow(x1 - x2,2)) +
						(math.pow(y1 - y2,2)))
	if distance <= 50:
		return True
	else:
		return False

def player(x, y):
	okno.blit(playerImage, (x - 16, y + 10))

def invader(x, y, i):
	okno.blit(invaderImage[i], (x, y))

def bullet(x, y):
	global bullet_state
	okno.blit(bulletImage, (x, y))
	bullet_state = "fire"
	
def kontrola_achievement():
	if score_val >= 25:
		return "Dosáhl skóre 25!"



running = True
while running:


	okno.fill((0, 0, 0))
	okno.blit(Pozadi.image, Pozadi.rect)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
			running = False
			


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_Xchange = -2.5
			if event.key == pygame.K_RIGHT:
				player_Xchange = 2.5
			if event.key == pygame.K_SPACE:
			
				
				if bullet_state == "rest":
					bullet_X = player_X
					bullet(bullet_X, bullet_Y)
					bullet_sound = mixer.Sound('images\strela.wav')
					bullet_sound.play()
		if event.type == pygame.KEYUP:
			player_Xchange = 0

	
	player_X += player_Xchange
	for i in range(no_of_invaders):
		invader_X[i] += invader_Xchange[i]

	
	if bullet_Y <= 0:
		bullet_Y = 650
		bullet_state = "rest"
	if bullet_state == "fire":
		bullet(bullet_X, bullet_Y)
		bullet_Y -= bullet_Ychange

	
	for i in range(no_of_invaders):
		
		

		if invader_X[i] >= 1000 or invader_X[i] <= 0:
			invader_Xchange[i] *= -1
			invader_Y[i] += invader_Ychange[i]
		
		collision = isCollision(bullet_X, invader_X[i],
								bullet_Y, invader_Y[i])
		if collision:
			score_val += 1
			bullet_Y = 650
			bullet_state = "rest"
			invader_X[i] = random.randint(64, 736)
			invader_Y[i] = random.randint(30, 200)
			invader_Xchange[i] *= -1

		invader(invader_X[i], invader_Y[i], i)
		if invader_Y[i] >= 600:
			if abs(player_X-invader_X[i]) < 80:
				for j in range(no_of_invaders):
					invader_Y[j] = 2000
				kontrola_achievement()
				game_over()






	if player_X <= 16:
		player_X = 1099
	elif player_X >= 1100:
		player_X = 17
    
    


	player(player_X, player_Y)
	show_score(scoreX, scoreY)
	pygame.display.update()
