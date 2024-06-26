import pygame
import requests
import json
import inspect
import hashlib
import os

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

    #print(users_info)
    return users_info

def get_users_owned_games(users_info):
    odpoved = requests.get(URL3)
    allOwnedGamesInfo = json.loads(odpoved.text)

    active_user_id = users_info["id"]

    hry_a_uzivatel = []

    for game in allOwnedGamesInfo:
        if game['user_id'] == active_user_id:
            game_id = game['game_id']
            hry_a_uzivatel.append(int(game_id))

    if hry_a_uzivatel:
        return hry_a_uzivatel

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

        if check_balance is not None:
            print(check_balance)

            try:
                with open(f"minihry/{game.location}/{game.file_name}.py", "rb") as file:
                    file_content = file.read()
            except:
                with open(f"minihry/{game.location}/source/{game.file_name}.py", "rb") as file:
                    file_content = file.read()

            hash_object = hashlib.sha256()
            hash_object.update(file_content)
            checksum = hash_object.hexdigest()

            print(checksum)

            data = {
                'username': user_information["username"],
                'game_name': game.name,
                'checksum': checksum,
                'achievement': str(check_balance),
            }

            url = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/get_money.php'

            #print('  Data se odesílají na server k ověření...')
            response = requests.post(url, json=data)
            vysledek = json.loads(response.text)['vysledek']

            print(f"               {vysledek}")

            # TODO: Flappybird a bageta potřebují změnu checksum



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

    
    #obsahuje id her, ktere aktivni uzivatel vlastni
    games_owned = get_users_owned_games(user_information)
    if games_owned == None:
        games_owned = []

    games = get_games(games_owned)


    for game in games:
        max_y += 57

    while running:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                running = False
                pygame.quit()

        user_information = library_draw(window, rozliseni, games, username_text, money_text, user_information, password)
        scrolling()
