import pygame
import sys
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

logo = pygame.image.load("images\SPSlogo.jpg")

#nastaví textové pole
text = ''
input_rect = pygame.Rect(300, 480, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_inactive = pygame.Color('gray15')
color = color_inactive
active = False

def login(rozliseni, window, clock):
    running = True
    clock.tick(60)
    global text, color, active

    while running:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicks on the input box
                if input_rect.collidepoint(udalost.pos):
                    active = not active
                else:
                    active = False
                # Change the color of the input box
                color = color_active if active else color_inactive
            if udalost.type == pygame.KEYDOWN:
                if active:
                    if udalost.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif udalost.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += udalost.unicode

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


        window.blit(logo, (rozliseni[0]/2 - 110, rozliseni[1]/2 - 200))

        #Vykreslení textu
        text_surface = font.render(text, True, color)
        width = max(200, text_surface.get_width() + 10)
        input_rect.w = width
        window.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(window, color, input_rect, 2)

        pos = pygame.mouse.get_pos()
        if Login.colliderect((pos[0], pos[1], 1, 1)) and pygame.mouse.get_pressed()[0]:
            completed_login = True
            running = False

        pygame.display.flip()

    completed_login = True
    return completed_login
