import pygame

# barvy
RED = (255, 0, 0)
BACKGROUND_COLOR = (0, 128, 195)
SECOND_BACKGROUND_COLOR = (0, 86, 132)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# texty
font = pygame.font.Font(None, 80)
smaller_font = pygame.font.Font(None, 40)
Timetable = "Knihovna"
Timetable_surface = font.render(Timetable, True, WHITE)
# username přihlášeného uživatele
username_text = smaller_font.render("username", True, WHITE)

y_difference = 0
last_mouse_y = 0


def scrolling():
    global y_difference, last_mouse_y

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)
            if event.button == 4:  # Scrolled up
                y_difference -= 10
            if event.button == 5:  # Scrolled down
                y_difference += 10
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y_difference < 0:
        y_difference += 10
    if keys[pygame.K_DOWN]:
        y_difference -= 10
    #print(y_difference)


def library_draw(window, rozliseni, games):
    global y_difference

    window.fill(BACKGROUND_COLOR)

    # zobrazování her
    x = 150
    y = 190
    game_number = 0

    # horní čára
    pygame.draw.rect(window, (0, 0, 0), (x - 75, y - 7, rozliseni[0] - 145, 2))

    for game in games:
        game.drawing(x, y, window, rozliseni, games[0+game_number].location, y_difference)

        y += 57
        game_number += 1

    pygame.draw.rect(window, BACKGROUND_COLOR, (0, 0, rozliseni[0], 183))

    # čára
    pygame.draw.rect(window, BLACK, (0, 110, 1300, 2))
    # texty
    window.blit(Timetable_surface, (25, 32))
    window.blit(username_text, (rozliseni[0] - 105 - username_text.get_width(), 55 - username_text.get_height()/2))
    # profilový obrázek
    pygame.draw.circle(window, BLACK, (rozliseni[0] - 55, 55), 40, 40)

    # překrytí her, spodní část
    pygame.draw.rect(window, BACKGROUND_COLOR, (0, rozliseni[1] - 185, rozliseni[0], 185))

    pygame.display.flip()


def library(rozliseni, window, clock):
    running = True
    clock.tick(60)

    from game_list import get_games
    games_owned = []
    games = get_games(games_owned)

    while running:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                running = False

        scrolling()
        library_draw(window, rozliseni, games)
