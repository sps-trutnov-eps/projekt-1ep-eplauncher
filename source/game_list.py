import pygame
import importlib
import inspect

BACKGROUND_COLOR = (0, 128, 195)
DARKER_BACKGROUND_COLOR = (0, 106, 164)


class Games:
    def __init__(self, jmeno_hry, popis_hry, cislo_hry, nazev_slozky, nazev_hlavni_funkce):
        self.name = jmeno_hry
        self.description = popis_hry
        self.id = cislo_hry
        self.location = nazev_slozky
        self.function_name = nazev_hlavni_funkce

    def drawing(self, x, y, window, rozliseni, nazev_slozky):
        velky_font = pygame.font.Font(None, 45)
        maly_font = pygame.font.Font(None, 25)
        titul_hry = velky_font.render(self.name, True, (0, 0, 0))
        popis_hry = maly_font.render(self.description, True, (255, 255, 255))

        #pozadí výběru hry
        play_button = pygame.Rect(int(x-15), int(y - 5), 615, 55)
        pygame.draw.rect(window, DARKER_BACKGROUND_COLOR, play_button)

        # zobrazení hry
        window.blit(titul_hry, (x, y))
        window.blit(popis_hry, (x, y + 30))
        pygame.draw.rect(window, (0, 0, 0), (x - 15, y + 50, rozliseni[0] - 185, 2))
        pygame.draw.rect(window, (0, 0, 0), (x - 15, y - 7, 2, 57))
        pygame.draw.rect(window, (0, 0, 0), (rozliseni[0] - 100, y - 7, 2, 59))

        #spouštění hry
        Games.startin_game(self, play_button, self.function_name)

    def startin_game(self, play_button, *args, **kwargs):
        pos = pygame.mouse.get_pos()

        # spouštěč hry
        if pygame.mouse.get_pressed()[0] and play_button.colliderect((pos[0], pos[1], 1, 1)):
            module_name = f"minihry.{self.location}.{self.function_name}"
            module = importlib.import_module(module_name)

            try:
                if self.function_name:
                    func = getattr(module, self.function_name)
                    return func(*args, **kwargs)

            except Exception as e:
                #print(f"Error executing module '{module_name}': {e}")
                # pokud není zadán název funkce -> spustit jako skript
                exec(module.__loader__.get_source(module.__name__))


def get_games():
    #sem vypisujte své hry ve formátu:
    # název hry, její popis, kolikátá je v pořadí (kdo dřív příjde ten dřív mele), název její složky,
    # název hlavní funkce (pokud je)

    # lze se řídit vzorem pokerun, poté co napíšete ten jeden řádek tak její název přidejte do listu games,
    # který je na konci

    # takto dlouhý text je limit!
    # 72 characters
    # pokud je delší, vymysli si kratší, nebo uprav kód

    # na konec svého kódu umistěte tyto dva řádky
    # screen = pygame.display.set_mode((800, 800))
    # pygame.display.set_caption("EPLauncher")
    # toto takto dělejte dokud nezjistim jak to opravit


    pokerun = Games("Pokérun", "Pokérun je skákací hra, ve které je hlavní cíl získat co nejvíce bodů.", 0, "Pokerun", "main")

    games = [pokerun]

    return games
