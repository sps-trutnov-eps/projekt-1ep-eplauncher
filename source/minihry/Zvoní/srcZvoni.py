import pygame, os, random

os.environ['SDL_VIDEO_CENTERED'] = '1'
#open the window in the middle of the screen
#sets resolution
okno = pygame.display.set_mode((1200, 800))

greyRectangle = pygame.image.load("source\minihry\Zvoní\Img\greyRectangle.png")
lineDark = (31, 77, 77)

FPS = 60
possiblePossition = [(75, 100-32), (75, 300-30), (75, 500-32), (75, 700-32)]
pozice = 2

canMove = True

movementTimer = 10 #frames
pocetRad = 1

listPrekazek = {"r1":[0,0,0,0]}
class Prekazky:
    def __init__(self, budePrekazka, listPrekazekVRade):
        self.budePrekazka = budePrekazka
        self.listPrekazekVRade = []

        for i in range(4):
            self.listPrekazekVRade.insert(0, random.randint(0,1))

    def printPrekazky(self, listPrekazekVRade):
        print(self.listPrekazekVRade)
        
 

run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    stisknuteKlavesy = pygame.key.get_pressed()

    okno.fill((50, 120, 120))

    for lines in range(4):
        pygame.draw.line(okno, lineDark, (0, 200*lines), (1200, 200*lines), 3)

    if stisknuteKlavesy[pygame.K_UP] and canMove == True:
        pozice -= 1
        canMove = False

    elif stisknuteKlavesy[pygame.K_DOWN] and canMove == True:
        pozice += 1
        canMove = False

    if pozice < 0:
        pozice = 0
    if pozice > 3:
        pozice = 3

    #TIMER FOR MOVEMENT
    if canMove == False:
        movementTimer -= 1 
        if movementTimer < 0:
            canMove = True
            movementTimer = 10

    if stisknuteKlavesy[pygame.K_SPACE]:
        listPrekazek.update("")

    print(pozice)
    okno.blit(greyRectangle, possiblePossition[pozice])

    pygame.display.update()
    pygame.time.Clock().tick(FPS) #framerate, FPS
