import pygame
import sys
import tkinter as tk  # For clipboard access on Windows

import requests
import json

pygame.init()

# barvy
red = (255, 0, 0)
loginButton = (200, 0, 10)
background_color = (0, 128, 195)
black = (0, 0, 0)
white = (225, 255, 255)

# texty
font = pygame.font.Font(None, 45)
jmeno = "jméno"
jmenoSurface = font.render(jmeno, True, white)
heslo = "heslo"
hesloSurface = font.render(heslo, True, white)
loginText = "Přihlásit"
loginTextSurface = font.render(loginText, True, white)

logo = pygame.image.load("minihry/Obrázky pro ostatní/Files/LOGO EPLauncher (transparentní).png")
logo = pygame.transform.scale(logo, (250, 250))

# nastaví textové pole pro psaní přihlašovacích údajů
username = ''
input_rect = pygame.Rect(300, 480, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_inactive = pygame.Color('gray15')
color = color_inactive
activeUsername = False
# Nastavení hesla
password = ''
inputPassword_rect = pygame.Rect(300, 550, 140, 32)
color_active1 = pygame.Color('lightskyblue3')
color_inactive1 = pygame.Color('gray15')
color1 = color_inactive1
activePassword = False
# Ukazuje se jen jako "*"
ShowPassword = ""
logged_in = False
register_font = pygame.font.Font(None, 25)
registration_text = register_font.render("vytvořit účet", True, white)


def get_clipboard_text():
    try:
        root = tk.Tk()
        root.withdraw()
        return root.clipboard_get()
    except tk.TclError:
        return ""


def login(rozliseni, window, clock):
    running = True
    clock.tick(60)
    global username, color, activeUsername, password, color1, activePassword, ShowPassword, logged_in

    register_button_rect = pygame.Rect(rozliseni[0] / 2 - 110, 690, 220, 30)

    completed_login = False

    icon = pygame.image.load("images/launcher_icon.png")
    pygame.display.set_icon(icon)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    activeUsername = not activeUsername
                else:
                    activeUsername = False
                color = color_active if activeUsername else color_inactive

                if inputPassword_rect.collidepoint(event.pos):
                    activePassword = not activePassword
                else:
                    activePassword = False
                color1 = color_active1 if activePassword else color_inactive1

                if Login.collidepoint(event.pos):
                    if login_check(username, password):
                        logged_in = True
                    else:
                        logged_in = False
                        print("Incorrect username or password!")  # Pokud je nesprávný login

                if register_button_rect.collidepoint(event.pos):
                    import registration_page
                    registered = registration_page.registration(window, rozliseni)

            if event.type == pygame.KEYDOWN:
                if activeUsername:
                    if event.key == pygame.K_RETURN:
                        username = ''
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                if activePassword:
                    if event.key == pygame.K_RETURN:
                        # Kubíček - "Měl by to být enter"
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        # Handle Backspace key
                        password = password[:-1]
                        ShowPassword = ShowPassword[:-1]
                    elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        # Handle Ctrl+V (paste) shortcut
                        clipboard_text = get_clipboard_text()
                        if clipboard_text:
                            # Clear the password first
                            password = ''
                            ShowPassword = ''
                            # Append the pasted text to the password
                            password += clipboard_text
                            ShowPassword += "*" * len(clipboard_text)
                    else:
                        # Add the pressed character to the password
                        password += event.unicode
                        ShowPassword += "*"

        window.fill(background_color)

        # vykreslí rámeček profilovky
        #profilovka = pygame.draw.rect(window, black, (rozliseni[0] / 2 - 110, rozliseni[1] / 2 - 200, 220, 220), 5)

        # lajny pro jméno a heslo
        pygame.draw.line(window, black, (rozliseni[0] / 2 - 110, 520), (rozliseni[0] / 2 + 110, 520), 5)
        pygame.draw.line(window, black, (rozliseni[0] / 2 - 110, 590), (rozliseni[0] / 2 + 110, 590), 5)

        # vykreslí přihlašovací tlačítko
        Login = pygame.draw.rect(window, loginButton, (rozliseni[0] / 2 - 110, 630, 220, 60))

        # vykresleni registracniho tlacitka
        window.blit(registration_text, (rozliseni[0] / 2 - registration_text.get_width()/2, 700))

        # vykreslí text
        if username == '':
            window.blit(jmenoSurface, (rozliseni[0] / 2 - 100, 480))
        if password == '':
            window.blit(hesloSurface, (rozliseni[0] / 2 - 100, 550))
        window.blit(loginTextSurface, (rozliseni[0] / 2 - loginTextSurface.get_width()/2, 645))

        window.blit(logo, (rozliseni[0] / 2 - logo.get_width()/2, rozliseni[1] / 2 - logo.get_height() + 20))

        # Vykresleni uzivatelem psaneho jmena
        username_surface = font.render(username, True, color)
        width = max(200, username_surface.get_width() + 10)
        input_rect.w = width
        window.blit(username_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(window, color, input_rect, 2)

        # Vykresleni uzivatelem psaneho hesla
        password_surface = font.render(ShowPassword, True, color)
        width = max(200, password_surface.get_width() + 10)
        inputPassword_rect.w = width
        window.blit(password_surface, (inputPassword_rect.x + 5, inputPassword_rect.y + 5))
        pygame.draw.rect(window, color1, inputPassword_rect, 2)

        pygame.display.flip()

        if logged_in:
            return True, username, password


def login_check(username, password):
    user = {'username': username, 'password': password}
    url = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/check_user.php'
    response = requests.post(url, json=user)

    response_data = json.loads(response.text)
    if isinstance(response_data['vysledek'], bool):
        return response_data['vysledek']
    elif response_data['vysledek'] == "Špatné heslo.":
        return False

