import pygame
import requests
import json

pygame.init()

# barvy
RED = (255, 0, 0)
BACKGROUND_COLOR = (0, 128, 195)
SECOND_BACKGROUND_COLOR = (0, 86, 132)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True

# texty
font = pygame.font.Font(None, 80)
smaller_font = pygame.font.Font(None, 40)
Timetable = "Knihovna"
Timetable_surface = font.render(Timetable, True, WHITE)
even_smaller_font = pygame.font.Font(None, 25)
# username přihlášeného uživatele


y_difference = 0
last_mouse_y = 0
max_y = 0

# urls
URL1 = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/users.php'
URL2 = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/add_user.php'
URL3 = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/owned.php'


def get_user_info(username):
    response = requests.get(URL1)
    user_info = json.loads(response.text)

    # Create a dictionary to store users' information with their usernames as keys
    users_dict = {user['username']: user for user in user_info}
    # Retrieve the user with the specified ID from the dictionary
    users_info = users_dict.get(username)

    
    return users_info

def get_users_owned_games():
    odpoved = requests.get(URL3)
    hry_info = json.loads(response.text)

    #dej to do slovniku, prirad s aktivnim userem (dle id) a pak to jen appendni do games_owned
    return True

def scrolling():
    global y_difference, last_mouse_y, running

    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            y_difference += int(event.y)*15

            if y_difference > 0:
                y_difference = 0

            elif y_difference < max_y * -1:
                y_difference = -max_y

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y_difference < 0:
        y_difference += 10
    if keys[pygame.K_DOWN] and y_difference > max_y * -1:
        y_difference -= 10


def library_draw(window, rozliseni, games, username_text, money_text, user_information, password):
    global y_difference, max_y

    window.fill(BACKGROUND_COLOR)

    # zobrazování her
    x = 150
    y = 190
    game_number = 0

    # horní čára
    pygame.draw.rect(window, (0, 0, 0), (x - 75, y - 7, rozliseni[0] - 145, 2))

    for game in games:
        check_balance = game.drawing(x, y, window, rozliseni, games[0+game_number].location, y_difference,
                                     user_money=user_information["money"],
                                     user_information=user_information,
                                     user_password=password)

        y += 57
        game_number += 1
        if check_balance:
            user_information = get_user_info(user_information["username"])

    pygame.draw.rect(window, BACKGROUND_COLOR, (0, 0, rozliseni[0], 183))

    # čára
    pygame.draw.rect(window, BLACK, (0, 110, 1300, 2))
    # texty
    window.blit(Timetable_surface, (25, 32))
    window.blit(username_text, (rozliseni[0] - 105 - username_text.get_width(), 55 - username_text.get_height()/2))
    window.blit(money_text, (rozliseni[0] - 105 - money_text.get_width(), 56 + money_text.get_height()/2))

    # profilový obrázek
    pygame.draw.circle(window, BLACK, (rozliseni[0] - 55, 55), 40, 40)

    # překrytí her, spodní část
    pygame.draw.rect(window, BACKGROUND_COLOR, (0, rozliseni[1] - 185, rozliseni[0], 185))

    pygame.display.flip()
    return user_information


def library(rozliseni, window, clock, username, password):
    global running, max_y
    clock.tick(60)

    username_text = smaller_font.render(username, True, WHITE)

    # obsahuje id, username, password, money
    user_information = get_user_info(username)

    money = user_information["money"]
    money_text_string = f"Mince: {money}"

    money_text = even_smaller_font.render(money_text_string, True, WHITE)

    from game_list import get_games



    games_owned = []   # TODO: do tohoto listu všechny ID her, který uživatel vlastní
    games = get_games(games_owned)


    for game in games:
        max_y += 57

    while running:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                running = False

        user_information = library_draw(window, rozliseni, games, username_text, money_text, user_information, password)
        scrolling()
