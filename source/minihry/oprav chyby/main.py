import pygame

pygame.init()
size = 1000, 600
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    