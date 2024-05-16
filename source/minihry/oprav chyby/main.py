import pygame

pygame.init()
size = 1000, 600
screen = pygame.display.set_mode(size)
running = True
opravovani = False
rules = False
clock = pygame.time.Clock()

title = pygame.image.load("obrázky/opraf_chiby2.png")
title_rect = title.get_rect(center = (500,150))
button = pygame.image.load("obrázky/hrat_button.png")
button_rect = button.get_rect(center = (500,450))

pravidla = pygame.image.load("obrázky/pravidla.png")
pravidla_rect = pravidla.get_rect(center = (900, 550))
rules_cross = pygame.image.load("obrázky/rules_end.png")
rules_cross_rect = rules_cross.get_rect(center = (940, 50))


while running:
    screen.fill((255,255,255))
    screen.blit(title, title_rect)
    screen.blit(button, button_rect)
    screen.blit(pravidla, pravidla_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                opravovani = True
            elif pravidla_rect.collidepoint(event.pos):
                rules = True 
            elif rules_cross_rect.collidepoint(event.pos):
                rules = False
                running = True 
    
    if opravovani:
        screen.fill((235,255,255))
    
    if rules:
        screen.fill((255,245,255))
        screen.blit(rules_cross, rules_cross_rect)
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    