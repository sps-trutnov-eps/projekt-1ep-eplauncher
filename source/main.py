import pygame, sys
pygame.init()

#nastaveni okna
resolution = [1300, 900]
pygame.display.set_caption("EPLauncher")
window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


#barvy
red = (255, 0, 0)
background = (80, 15, 255)
black = (0, 0, 0)
white = (255, 255, 255)


#texty
font = pygame.font.Font(None, 45)
Timetable = "knihovna"
Timetable_surface = font.render(Timetable, True, white)


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(background)
    pygame.draw.rect(window,black, (0, 130, 1300, 2))
    window.blit(Timetable_surface, (60, 100))

    pygame.display.update()
    clock.tick(60)