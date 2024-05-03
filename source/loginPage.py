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

# nastaví textové pole pro psaní přihlašovacích údajů
username = ''
input_rect = pygame.Rect(300, 480, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_inactive = pygame.Color('gray15')
color = color_inactive
activeUsername = False
#Nastavení hesla
password = ''
inputPassword_rect = pygame.Rect(300, 550, 140, 32)
color_active1 = pygame.Color('lightskyblue3')
color_inactive1 = pygame.Color('gray15')
color1 = color_inactive1
activePassword = False
#Ukazuje se jen jako "*"
ShowPassword = ""


def login_check(username, password):
    # request info
    
    # go through the info
    
    #if username == requested_username and password == requested_password:
    #    logged_in = True
    
    return True


def login(rozliseni, window, clock):
    running = True
    clock.tick(60)
    global username, color, activeUsername, password, color1, activePassword, ShowPassword

    while running:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if udalost.type == pygame.MOUSEBUTTONDOWN:# Toto je pro prihlasovaci jmeno
                # If the user clicks on the input box
                if input_rect.collidepoint(udalost.pos):
                    activeUsername = not activeUsername
                else:
                    activeUsername = False
                # Change the color of the input box
                color = color_active if activeUsername else color_inactive
            if udalost.type == pygame.KEYDOWN:
                if activeUsername:
                    if udalost.key == pygame.K_RETURN:
                        username = ''
                    elif udalost.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += udalost.unicode
            # Toto je pro heslo
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicks on the input box
                if inputPassword_rect.collidepoint(udalost.pos):
                    activePassword = not activePassword
                else:
                    activePassword = False
                # Change the color of the input box
                color1 = color_active1 if activePassword else color_inactive1
            if udalost.type == pygame.KEYDOWN:
                if activePassword:
                    if udalost.key == pygame.K_RETURN:
                        password = ''
                        SShowPassword = ""
                    elif udalost.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                        ShowPassword = ShowPassword[:-1]
                    else:
                        password += udalost.unicode
                        ShowPassword += "*"
                        if udalost.key == pygame.K_LSHIFT:
                            ShowPassword = ShowPassword[:-1]
        

        window.fill(background_color)
        #vykreslí rámeček profilovky
        profilovka = pygame.draw.rect(window, black, (rozliseni[0]/2 - 110, rozliseni[1]/2 - 200, 220, 220), 5)
        #lajny pro jméno a heslo
        pygame.draw.line(window, black, (rozliseni[0]/2 - 110, 520), (rozliseni[0]/2 + 110, 520), 5)
        pygame.draw.line(window, black, (rozliseni[0] / 2 - 110, 590), (rozliseni[0] / 2 + 110, 590), 5)
        #vykreslí přihlašovací tlačítko
        Login = pygame.draw.rect(window, loginButton, (rozliseni[0] / 2 - 110, 630, 220, 60))
        #vykreslí text
        if username == '':
            window.blit(jmenoSurface, (rozliseni[0]/2 - 100, 480))
        if password == '':
            window.blit(hesloSurface, (rozliseni[0]/2 - 100, 550))
        window.blit(loginTextSurface, (rozliseni[0] / 2 - 100, 645))


        window.blit(logo, (rozliseni[0]/2 - 110, rozliseni[1]/2 - 200))

        #Vykresleni uzivatelem psaneho jmena
        username_surface = font.render(username, True, color)
        width = max(200, username_surface.get_width() + 10)
        input_rect.w = width
        window.blit(username_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(window, color, input_rect, 2)
        
        #Vykresleni uzivatelem psaneho hesla
        password_surface = font.render(ShowPassword, True, color)
        width = max(200, password_surface.get_width() + 10)
        inputPassword_rect.w = width
        window.blit(password_surface, (inputPassword_rect.x + 5, inputPassword_rect.y + 5))
        pygame.draw.rect(window, color1, inputPassword_rect, 2)
        

        pos = pygame.mouse.get_pos()
        if Login.colliderect((pos[0], pos[1], 1, 1)) and pygame.mouse.get_pressed()[0]:
            login_check()
            
            if logged_in:
                completed_login = True
                running = False

        pygame.display.flip()

    completed_login = True
    return completed_login
