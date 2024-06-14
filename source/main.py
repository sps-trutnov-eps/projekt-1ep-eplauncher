def main():
    import pygame
    import loginPage
    import library_menu
    pygame.init()

    #nastaveni okna
    rozliseni = [800, 800]
    pygame.display.set_caption("EPLauncher")
    window = pygame.display.set_mode(rozliseni)
    clock = pygame.time.Clock()
    icon = pygame.image.load("images/launcher_icon.png")

    pygame.display.set_icon(icon)

    completed_login = False
    if not completed_login:
        completed_login, username, password = loginPage.login(rozliseni, window, clock)
    if completed_login:
        library_menu.library(rozliseni, window, clock, username, password)


if __name__ == "__main__":
    main()