
import pygame  
import sys  
  
  
# initializing the constructor  
pygame.init()  
  
# screen resolution  
res = (700,700)  
  
# opens up a window  
okno = pygame.display.set_mode(res)  
  
# white color  
color = (255,255,255)  
  
# light shade of the button  
color_light = (170,170,170)  
  
# dark shade of the button  
color_dark = (100,100,100)  
  
# stores the width of the  
# screen into a variable  
width = okno.get_width()  
  
# stores the height of the  
# screen into a variable  
height = okno.get_height()  
  
bigfont = pygame.font.SysFont('arial',50) 
smallfont = pygame.font.SysFont('corbel',35)  
nazev = bigfont.render('Mhunt', True, color) 
  
text = smallfont.render('Hrát' , True , color)  
  
while True:  
      
    for ev in pygame.event.get():  
          
        if ev.type == pygame.QUIT:  
            pygame.quit()  
              
        #checks if a mouse is clicked  
        if ev.type == pygame.MOUSEBUTTONDOWN:  
              
            #if the mouse is clicked on the  
            # button the game is terminated  
            if width/2-70 <= mys[0] <= width/2+70 and height/2 <= mys[1] <= height/2+40:  
                open('Mhunt.py')
                pygame.quit()  
                  
    # fills the screen with a color  
    okno.fill((60,25,60))  
      
    # stores the (x,y) coordinates into  
    # the variable as a tuple  
    mys = pygame.mouse.get_pos()  
      
    # if mouse is hovered on a button it  
    # changes to lighter shade  
    if width/2-70 <= mys[0] <= width/2+70 and height/2 <= mys[1] <= height/2+40:  
        pygame.draw.rect(okno,color_light,[width/2-70,height/2,140,40])  
          
    else:  
        pygame.draw.rect(okno,color_dark,[width/2-70,height/2,140,40])  
      
    # superimposing the text onto our button  
    okno.blit(text , (width/2-30,height/2))  
    okno.blit(nazev, (width/2-70,height/4))  
    # updates the frames of the game  
    pygame.display.update() 