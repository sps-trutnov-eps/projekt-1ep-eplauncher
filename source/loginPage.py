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
        #Human input

def Prihlaseni():
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        window.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(window, color, input_box, 2)

        window.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Blit the text.
        window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(window, color, input_box, 2)

        

        pos = pygame.mouse.get_pos()
        if Login.colliderect((pos[0], pos[1], 1, 1)) and pygame.mouse.get_pressed()[0]:
            completed_login = False
            running = False


    completed_login = True
    return completed_login
