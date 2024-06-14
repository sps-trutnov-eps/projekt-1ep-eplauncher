import pygame, os, random, threading
pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
#open the window in the middle of the screen
#sets resolution
okno = pygame.display.set_mode((1200, 800))


gameOver = False
def main():
    global rychlostPrekazky, offsetDvery, dvere, listPrekazek, pozice, WinningPrekazek, pocetSmazanychPrekazek, pozice1X, pozice1Y, okno, goodEngingCheck, possiblePossition, gameOver


    greyRectangle = pygame.image.load("source/minihry/Zvoni/Img/ucitel.png")
    greyRectangle = pygame.transform.scale(greyRectangle, (80,80))
    dvere = pygame.image.load("source/minihry/Zvoni/Img/dvere.png")
    lineDark = (247, 159, 0)
    
    student1 = pygame.image.load("source/minihry/Zvoni/Img/student.png")
    student1 = pygame.transform.scale(student1, (80, 80))
    student2 = pygame.image.load("source/minihry/Zvoni/Img/student2.png")
    student2 = pygame.transform.scale(student2, (80, 80))
    student3 = pygame.image.load("source/minihry/Zvoni/Img/student3.png")
    student3 = pygame.transform.scale(student3, (80, 80))

    FPS = 120

    pozice1X = 75
    pozice1Y = 300-32
    possiblePossition = [(75, 100-32), (pozice1X, pozice1Y), (75, 500-32), (75, 700-32)]
    pozice = 2

    canMove = True
    movementTimer = 20 #frames

    rychlostPrekazky = 5

    pocetSmazanychPrekazek = 0
    WinningPrekazek = 15
    xLine = 1200  
    offsetDvery = 0
    goodEngingCheck = 0
    listPrekazek = []
    
    ZvoniAchivement = False
    
    class Prekazky:
        global pozice
        def __init__(self):
            self.pozice = random.randint(0,3)
            self.poziceX = 1400
            
            self.textura = random.randint(1,3)
            
            
        def PohybPrekazky(self):
            self.poziceX -= rychlostPrekazky
            

        def vykresleniPrekazky(self):
            global pocetSmazanychPrekazek
            if pocetSmazanychPrekazek <= WinningPrekazek:
                prekazkaRect = pygame.Rect(self.poziceX, ((200*self.pozice)+64), 64, 64)
                #pygame.draw.rect(okno, (185,122,86), prekazkaRect)

                if self.textura == 1:
                    okno.blit(student1, (prekazkaRect[0], prekazkaRect[1]))
                elif self.textura == 2:
                    okno.blit(student2, (prekazkaRect[0], prekazkaRect[1]))
                elif self.textura == 3:
                    okno.blit(student3, (prekazkaRect[0], prekazkaRect[1]))

        def outOfBounds(self):
            global pocetSmazanychPrekazek
            if self.poziceX < -64:
                for i,o in enumerate(listPrekazek):
                    del listPrekazek[i]
                    pocetSmazanychPrekazek += 1
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
        if pocetSmazanychPrekazek <= WinningPrekazek:
            threading.Timer(0.8, SpawnPrekazek).start()
            for i in range(3):
                listPrekazek.append(
                    Prekazky()
                )
    
    def FontChoossenSize(font, size):
        return pygame.font.SysFont(font, size)

    def konecnaAnimace():
        global offsetDvery, pozice1Y, pozice1X, possiblePossition, goodEngingCheck
        if offsetDvery <= 200:
            offsetDvery += 1
        okno.blit(dvere, (1200 - offsetDvery,0))
        
        if pozice1Y <= 350:
            pozice1Y += 0.25
            
        if pozice1X <= 850:
            pozice1X += 0.5
        else:
            goodEngingCheck = 1

        possiblePossition = [(75, 100-32), (pozice1X, pozice1Y), (75, 500-32), (75, 700-32)]


    SpawnPrekazek()
    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        stisknuteKlavesy = pygame.key.get_pressed()

        okno.fill((250, 206, 112))

        if stisknuteKlavesy[pygame.K_UP] or stisknuteKlavesy[pygame.K_w] and canMove == True:
            pozice -= 1
            canMove = False

        elif stisknuteKlavesy[pygame.K_DOWN] or stisknuteKlavesy[pygame.K_s] and canMove == True: 
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
                movementTimer = 20
                
        if pocetSmazanychPrekazek >= WinningPrekazek:
            canMove = False
            pozice = 1

        if gameOver == False and pocetSmazanychPrekazek <= WinningPrekazek:
            for lines in range(4):
                pygame.draw.line(okno, lineDark, (0, 200*lines), (1200, 200*lines), 4)


        for i in listPrekazek:
            if gameOver == False and pocetSmazanychPrekazek <= WinningPrekazek:
                i.KontrolaKolize()
                i.outOfBounds()
                i.vykresleniPrekazky()
                i.PohybPrekazky()
            if gameOver == True:
                
                gameOverFont = FontChoossenSize("Verdana", 50).render("Narazil jsi do studenta!", True, (220,20,20))
                okno.blit(gameOverFont, (300, 350))

                #any key pressed
                if event.type == pygame.KEYDOWN:
                    gameOver = False
                    pozice = 2
                    listPrekazek.clear()
                    pocetSmazanychPrekazek = 1
                
            if pocetSmazanychPrekazek >= WinningPrekazek:
                if xLine >= 0:
                    xLine -= 0.75
                    
                    for lines in range(4):
                        pygame.draw.line(okno, lineDark, (0, 200*lines), (xLine, 200*lines), 4)
                else:
                    konecnaAnimace()


        okno.blit(greyRectangle, possiblePossition[pozice])
        
        if goodEngingCheck == 1:
            goodEndingFont = FontChoossenSize("Verdana", 50).render("Dostal jsi se do třídy na čas!", True, (220,20,20))
            okno.blit(goodEndingFont, (250, 350))
            ZvoniAchivement = True

        pygame.display.update()
        pygame.time.Clock().tick(FPS) #framerate, FPS

    if ZvoniAchivement == True:
        return True, "Zvoni"
        
if __name__ == "__main__":
    main()


