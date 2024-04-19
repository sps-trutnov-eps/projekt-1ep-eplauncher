import pygame, sys
pygame.init()

#barvy
red = (255, 0, 0)
loginButton = (200, 0, 10)
background_color = (0, 128, 195)
black = (0, 0, 0)
white = (225, 255, 255)

#texty
font = pygame.font.Font(None, 45)
jmeno = "jméno"
jmenoSurface = font.render(jmeno, True, white)
heslo = "heslo"
hesloSurface = font.render(heslo, True, white)
loginText = "login"
loginTextSurface = font.render(loginText, True, white)


def login(rozliseni, window, clock):
    running = True
    clock.tick(60)

    while running:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(background_color)
        #vykreslí rámeček profilovky
        profilovka = pygame.draw.rect(window, black, (rozliseni[0]/2 - 110, rozliseni[1]/2 - 200, 220, 220), 5)
        #lajny pro jméno a heslo
        pygame.draw.line(window, black, (rozliseni[0]/2 - 110, 520), (rozliseni[0]/2 + 110, 520), 5)
        pygame.draw.line(window, black, (rozliseni[0] / 2 - 110, 590), (rozliseni[0] / 2 + 110, 590), 5)
        #vykreslí přihlašovací tlačítko
        Login = pygame.draw.rect(window, loginButton, (rozliseni[0] / 2 - 110, 630, 220, 60))
        #vykreslí text
        window.blit(jmenoSurface, (rozliseni[0]/2 - 100, 480))
        window.blit(hesloSurface, (rozliseni[0]/2 - 100, 550))
        window.blit(loginTextSurface, (rozliseni[0] / 2 - 100, 645))

        pos = pygame.mouse.get_pos()
        if Login.colliderect((pos[0], pos[1], 1, 1)) and pygame.mouse.get_pressed()[0]:
            completed_login = False
            running = False

        pygame.display.flip()

    completed_login = True
    return completed_login
