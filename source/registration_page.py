import pygame
import sys
import requests
import json
import tkinter as tk

pygame.init()

# barvy
red = (255, 0, 0)
loginButton_color = (200, 0, 10)
background_color = (0, 128, 195)
black = (0, 0, 0)
white = (225, 255, 255)

# texty
font = pygame.font.Font(None, 45)
jmeno = "jméno"
jmenoSurface = font.render(jmeno, True, white)
heslo = "heslo"
hesloSurface = font.render(heslo, True, white)
loginText = "Zaregistrovat"
loginTextSurface = font.render(loginText, True, white)

logo = pygame.image.load("images\SPSlogo.jpg")

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
registered = False
URL1 = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/add_user.php'
URL2 = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/users.php'


def get_clipboard_text():
    try:
        root = tk.Tk()
        root.withdraw()
        return root.clipboard_get()
    except tk.TclError:
        return ""


def registration(window, rozliseni):
    global username, color, activeUsername, password, color1, activePassword, ShowPassword, registered

    register_button = pygame.draw.rect(window, loginButton_color, (rozliseni[0] / 2 - 110, 630, 220, 60))

    running = True

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

                if register_button.collidepoint(event.pos):
                    if register_the_user(username, password):
                        registered = True

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
                        pass
                    elif event.key == pygame.K_BACKSPACE:
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

        registration_draw(window, rozliseni)

        if registered:
            return True


def registration_draw(window, rozliseni):
    window.fill(background_color)

    # vykreslí rámeček profilovky
    profilovka = pygame.draw.rect(window, black, (rozliseni[0] / 2 - 110, rozliseni[1] / 2 - 200, 220, 220), 5)

    # lajny pro jméno a heslo
    pygame.draw.line(window, black, (rozliseni[0] / 2 - 110, 520), (rozliseni[0] / 2 + 110, 520), 5)
    pygame.draw.line(window, black, (rozliseni[0] / 2 - 110, 590), (rozliseni[0] / 2 + 110, 590), 5)

    # vykreslí přihlašovací tlačítko
    register_button = pygame.draw.rect(window, loginButton_color, (rozliseni[0] / 2 - 110, 630, 220, 60))

    # vykreslí text
    if username == '':
        window.blit(jmenoSurface, (rozliseni[0] / 2 - 100, 480))
    if password == '':
        window.blit(hesloSurface, (rozliseni[0] / 2 - 100, 550))
    window.blit(loginTextSurface, (rozliseni[0] / 2 - loginTextSurface.get_width()/2, 645))

    window.blit(logo, (rozliseni[0] / 2 - 110, rozliseni[1] / 2 - 200))

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


def register_the_user(username, password):
    user = {'username': username, 'password': password}

    try:
        response = requests.post(URL1, json=user)
        return True
    except:
        print("Failed to run")
        return False
