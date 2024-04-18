import pygame
import sys
pygame.init()

#barvy
RED = (255, 0, 0)
BACKGROUND_COLOR = (0, 128, 195)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#texty
font = pygame.font.Font(None, 45)
Timetable = "knihovna"
Timetable_surface = font.render(Timetable, True, WHITE)
# username přihlášeného uživatele
username_text = font.render("username", True, WHITE)


def main():
    # nastaveni okna
    resolution = [1300, 900]
    pygame.display.set_caption("EPLauncher")
    window = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()

    while True:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(BACKGROUND_COLOR)
        pygame.draw.rect(window, BLACK, (0, 130, 1300, 2))
        # texty
        window.blit(Timetable_surface, (60, 100))
        # profilový obrázek
        pygame.draw.circle(window, BLACK, (resolution[0] - 75, 65), 50, 50)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()