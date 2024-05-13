import sys
import pygame
pygame.init()

rozliseni_okna = (1500, 768)
okno = pygame.display.set_mode(rozliseni_okna)
#----------------------------------------------------------------------
zluta = (255,215,0)
cash = 100
kytkacena = "50 - Q"
strileccena = "50 - W"
zedcena = "100 - E"
font = pygame.font.SysFont(None, 50)    # pripava pro text penez
fontcena = pygame.font.SysFont(None, 30)    # font pro cenu
timer = pygame.time.get_ticks()          # casovac k pricitani penez
cas = pygame.time.Clock()
cashplus = 5000      # cas pro pricteni penez - 1000 = 1 sekunda
#----------------------------------------------------------------------
herni_ctverce = [pygame.Rect(150 * i, 192 * j, 150, 192) for i in range(8) for j in range(4)]
vyber_ctverce = [pygame.Rect(1320, 50 + 150 * j, 180, 150) for j in range(3)]



kytka = pygame.image.load('kytka.png')
strilec = pygame.image.load('strilec.png')
zed = pygame.image.load('zed.png')
#----------------------------------------------------------------------
aktivni_ctverec = None
aktivni_obrazek = None
index_vybraneho_ctverce = None


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif udalost.type == pygame.MOUSEBUTTONDOWN:
            pozice = pygame.mouse.get_pos()
            for i, ctverec in enumerate(herni_ctverce):
                if ctverec.collidepoint(pozice):
                    if aktivni_obrazek is not None and index_vybraneho_ctverce is not None:
                        okno.blit(pygame.image.load(aktivni_obrazek + 'strilec.png'), (herni_ctverce[index_vybraneho_ctverce].x, herni_ctverce[index_vybraneho_ctverce].y))
                        print(f"Umístění obrázku {aktivni_obrazek} na čtverec č.{index_vybraneho_ctverce}")
                        index_vybraneho_ctverce = None
                    else:
                        print(f"Kliknuto na herní čtverec č.{i}")
                        index_vybraneho_ctverce = i
            for j, vyber_ctverce_single in enumerate(vyber_ctverce):
                if vyber_ctverce_single.collidepoint(pozice):
                    aktivni_obrazek = f"obrazek_{j}"
            
                
    
    
    
    timer2 = pygame.time.get_ticks()      # pricitani penez
    if timer2 - timer > cashplus:
        cash += 10
        timer = timer2

     
#----------------------------------------------------------------------   
    
    
    
    okno.fill((34,139,34))                  
    penize = font.render(str(cash), True, zluta)     # text penez
    cenakytky = fontcena.render(str(kytkacena), True, zluta)
    cenastrilec = fontcena.render(str(strileccena), True, zluta)
    cenazed = fontcena.render(str(zedcena), True, zluta)
#----------------------------------------------------------------------
    
    
    
    
    pygame.draw.rect(okno, (255,255,255), (0,192,1320,1))
    pygame.draw.rect(okno, (255,255,255), (0,192*2,1320,1)) 
    pygame.draw.rect(okno, (255,255,255), (0,192*3,1320,1))     
    pygame.draw.rect(okno, (0,0,0), (150,0,1,768))       
    pygame.draw.rect(okno, (0,0,0), (150*2,0,1,768)) 
    pygame.draw.rect(okno, (0,0,0), (150*3,0,1,768)) 
    pygame.draw.rect(okno, (0,0,0), (150*4,0,1,768))
    pygame.draw.rect(okno, (0,0,0), (150*5,0,1,768))
    pygame.draw.rect(okno, (0,0,0), (150*6,0,1,768))
    pygame.draw.rect(okno, (0,0,0), (150*7,0,1,768))
    pygame.draw.rect(okno, (0,0,0), (150*8,0,1,768))
    pygame.draw.rect(okno, (139,69,19), (1320,0,180,768))
    pygame.draw.rect(okno, (0,0,0), (1320,50,180,1))
    okno.blit(penize, (1320,20))
    okno.blit(kytka, (1380, 100)) # obrazek
    okno.blit(cenakytky, (1390, 150))  # cena
    okno.blit(cenastrilec, (1390, 300))  #cena
    okno.blit(strilec, (1380, 250))  # obrazek
    okno.blit(zed, (1380, 400))  # obrazek
    okno.blit(cenazed, (1390, 450))  # cena
    
    pygame.draw.rect(okno, (0,0,0), (1320, 200, 300, 1))
    pygame.draw.rect(okno, (0,0,0), (1320, 350, 300, 1))
    pygame.draw.rect(okno, (0,0,0), (1320, 500, 300, 1))
    pygame.draw.rect(okno, (0,0,0), (1320, 0, 1, 500))
#----------------------------------------------------------------------          
    pygame.display.update()