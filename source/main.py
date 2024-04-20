def main():
    import pygame
    import sys
    import loginPage
    import library_menu
    pygame.init()

    #nastaveni okna
    rozliseni = [800, 800]
    pygame.display.set_caption("EPLauncher")
    window = pygame.display.set_mode(rozliseni)
    clock = pygame.time.Clock()

    completed_login = False
    if not completed_login:
        completed_login = loginPage.login(rozliseni, window, clock)
    if completed_login:
        library_menu.library(rozliseni, window, clock)


if __name__ == "__main__":
    main()