import pygame, os, random, threading
pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
#open the window in the middle of the screen
#sets resolution
okno = pygame.display.set_mode((1200, 800))

greyRectangle = pygame.image.load("Img\greyRectangle.png")
dvere = pygame.image.load("Img\dvere.png")
lineDark = (31, 77, 77)

FPS = 60
possiblePossition = [(75, 100-32), (75, 300-32), (75, 500-32), (75, 700-32)]
pozice = 2

canMove = True
movementTimer = 10 #frames

gameOver = False
rychlostPrekazky = 10

pocetSmazanychPrekazek = 0
WinningPrekazek = 5
xLine = 1200  
offsetDvery = 0

def FontChoossenSize(font, size):
    return pygame.font.SysFont(font, size)

def konecnaAnimace():
    global offsetDvery
    if offsetDvery <= 200:
        offsetDvery += 1
    okno.blit(dvere, (1200 - offsetDvery,0))
    pass


listPrekazek = []
class Prekazky:
    def __init__(self):
        self.pozice = random.randint(0,3)
        self.poziceX = 1400
        
        
    def PohybPrekazky(self):
        self.poziceX -= rychlostPrekazky
        

    def vykresleniPrekazky(self):
        global pocetSmazanychPrekazek
        if pocetSmazanychPrekazek <= WinningPrekazek:
            prekazkaRect = pygame.Rect(self.poziceX, (200*self.pozice)+68, 64, 64)
            pygame.draw.rect(okno, (255,0,0), prekazkaRect)
        
    def outOfBounds(self):
        global pocetSmazanychPrekazek
        if self.poziceX < -64:
            for i,o in enumerate(listPrekazek):
                del listPrekazek[i]
                pocetSmazanychPrekazek += 1
                print(pocetSmazanychPrekazek)
                break
            
    def KontrolaKolize(self):
        global gameOver

    #sets rectangle value for every object on screen
        hraceRect = pygame.Rect(possiblePossition[pozice][0],possiblePossition[pozice][1], 64 ,64)
        for prekazky in listPrekazek:
            prekazkaRect = pygame.Rect(prekazky.poziceX, prekazky.pozice*200, 64, 80)

            if pygame.Rect.colliderect(hraceRect, prekazkaRect): #když kolize
                gameOver = True


def SpawnPrekazek():
    threading.Timer(0.8, SpawnPrekazek).start()
    for i in range(3):
        listPrekazek.append(
            Prekazky()
        )
SpawnPrekazek()

run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    stisknuteKlavesy = pygame.key.get_pressed()

    okno.fill((50, 120, 120))


    if stisknuteKlavesy[pygame.K_UP] and canMove == True:
        pozice -= 1
        canMove = False

    elif stisknuteKlavesy[pygame.K_DOWN] and canMove == True:
        pozice += 1
        canMove = False

    if stisknuteKlavesy[pygame.K_g]:
        pass

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
            
    if pocetSmazanychPrekazek >= WinningPrekazek:
        canMove = False
        pozice = 1

    if gameOver == False and pocetSmazanychPrekazek <= WinningPrekazek:
        for lines in range(4):
            pygame.draw.line(okno, lineDark, (0, 200*lines), (1200, 200*lines), 3)


    for i in listPrekazek:
        if gameOver == False and pocetSmazanychPrekazek <= WinningPrekazek:
            i.KontrolaKolize()
            i.vykresleniPrekazky()
            i.PohybPrekazky()
            i.outOfBounds()
        elif gameOver == True:
            
            gameOverFont = FontChoossenSize("Verdana", 50).render("Game Over", True, (220,20,20))
            okno.blit(gameOverFont, (450, 350))
            
        if pocetSmazanychPrekazek >= WinningPrekazek:
            if xLine >= 0:
                xLine -= 0.75
                print(xLine)
                
                for lines in range(4):
                    pygame.draw.line(okno, lineDark, (0, 200*lines), (xLine, 200*lines), 3)
            else:
                konecnaAnimace()



    okno.blit(greyRectangle, possiblePossition[pozice])

    pygame.display.update()
    pygame.time.Clock().tick(FPS) #framerate, FPS
