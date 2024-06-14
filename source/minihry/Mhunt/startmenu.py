
import pygame  
import sys  
  
  
 
pygame.init()  
  
  
res = (700,700)  
  
  
okno = pygame.display.set_mode(res)  
  
  
color = (255,255,255)  
  
 
color_light = (170,170,170)  
  
  
color_dark = (100,100,100)  
  
  
width = okno.get_width()  
  
  
height = okno.get_height()  
smalfont = pygame.font.SysFont("corbel",30)  
bigfont = pygame.font.SysFont('arial',50) 
smallfont = pygame.font.SysFont('corbel',35)  
nazev = bigfont.render('Mhunt', True, color) 
ovladani = smalfont.render("pohyb do prava a do leva šipkami střílení spacebarem",True, color)





text = smallfont.render('Hrát' , True , color)  
def startmenu():
    
    running = True   
    while running:  
          
        for ev in pygame.event.get():  
              
            if ev.type == pygame.QUIT:  
                running = False
                pygame.quit()
                quit() 
                
        
                
         
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                  
     
                if width/2-70 <= mys[0] <= width/2+70 and height/2 <= mys[1] <= height/2+40:  
                    from Mhunt import mhunt_game
                    mhunt_game()
                    running = False
                    
                       
                      
       
        okno.fill((60,25,60))  
         
        mys = pygame.mouse.get_pos()  
          
      
        if width/2-70 <= mys[0] <= width/2+70 and height/2 <= mys[1] <= height/2+40:  
            pygame.draw.rect(okno,color_light,[width/2-70,height/2,140,40])  
              
        else:  
            pygame.draw.rect(okno,color_dark,[width/2-70,height/2,140,40])  
          
      
        okno.blit(text , (width/2-30,height/2))  
        okno.blit(nazev, (width/2-60,height/4))  
        okno.blit(ovladani, (width/18, height/3)) 
        pygame.display.update() 
if __name__ == "__main__":
    startmenu()
    