import pygame
import importlib
import json
import requests

BACKGROUND_COLOR = (0, 128, 195)
DARKER_BACKGROUND_COLOR = (0, 106, 164)

URL = 'http://senkyr.epsilon.spstrutnov.cz/eplauncher/api/buy_game.php'


class Games:
    def __init__(self, jmeno_hry, popis_hry, cislo_hry, nazev_slozky, nazev_souboru, nazev_hlavni_funkce, uzamcena, cena):
        self.name = jmeno_hry
        self.description = popis_hry
        self.id = cislo_hry
        self.location = nazev_slozky
        self.function_name = nazev_hlavni_funkce
        self.locked = uzamcena
        self.owned = False
        self.cost = cena
        self.file_name = nazev_souboru

    def drawing(self, x, y, window, rozliseni, nazev_slozky, y_difference, user_money, user_information, user_password):
        velky_font = pygame.font.Font(None, 45)
        maly_font = pygame.font.Font(None, 25)
        titul_hry = velky_font.render(self.name, True, (0, 0, 0))
        popis_hry = maly_font.render(self.description, True, (255, 255, 255))

        locked_game_icon = pygame.image.load("images/locked.png")

        try:
            icon = pygame.transform.scale(pygame.image.load(f"minihry/{self.location}/icon.png"), (55, 55))
        except:
            icon = pygame.image.load("images/missing_icon.png")

        # pozadí výběru hry
        play_button = pygame.Rect(int(x-15), int(y - 5 + y_difference), 595, 55)
        pygame.draw.rect(window, DARKER_BACKGROUND_COLOR, play_button)

        # zobrazení hry
        window.blit(titul_hry, (x, y + y_difference))
        window.blit(popis_hry, (x, y + 30 + y_difference))

        window.blit(icon, (x - 73, y - 5 + y_difference))
        if self.locked:
            window.blit(locked_game_icon, (x - 73, y - 5 + y_difference))

        # čára rozdělující ikonu hry a popis hry
        pygame.draw.rect(window, (0, 0, 0), (x - 18, y - 5 + y_difference, 2, 55))
        # spodní krajní čára pro hru
        pygame.draw.rect(window, (0, 0, 0), (x - 75, y + 50 + y_difference, rozliseni[0] - 145, 2))
        # levá krajní čára pro hru
        pygame.draw.rect(window, (0, 0, 0), (x - 75, y - 7 + y_difference, 2, 57))
        # pravá krajní čára pro hru
        pygame.draw.rect(window, (0, 0, 0), (rozliseni[0] - 70, y - 7 + y_difference, 2, 59))

        # spouštění hry
        check_balance = Games.startin_game(self, play_button, user_money, user_information, user_password,
                                           self.function_name)
        return check_balance

    def startin_game(self, play_button, user_money, user_information, user_password, *args, **kwargs):
        pos = pygame.mouse.get_pos()

        # spouštěč hry
        if pygame.mouse.get_pressed()[0] and play_button.colliderect((pos[0], pos[1], 1, 1)):
            if not self.locked:
                try:
                    module_name = f"minihry.{self.location}.{self.file_name}"
                    module = importlib.import_module(module_name)
                except:
                    module_name = f"minihry.{self.location}.source.{self.file_name}"
                    module = importlib.import_module(module_name)

                if self.function_name is None:
                    # pokud není zadán název funkce -> spustit jako skript
                    exec(module.__loader__.get_source(module.__name__))

                else:
                    try:
                        func = getattr(module, self.function_name)
                        return func()

                    except Exception as e:
                        print(f"Error executing module '{module_name}': {e}")

                        # když stejně nic nefunguje, spustit jako skript
                        exec(module.__loader__.get_source(module.__name__))

                window = pygame.display.set_mode((800, 800))
                pygame.display.set_caption("EPLauncher")

            elif self.locked:
                #print("locked game")
                if int(self.cost) <= int(user_money):
                    #print("purchasing")
                    game_id = self.id
                    username = user_information["username"]
                    password = user_password

                    try:
                        # Send the POST request
                        response = requests.post(URL, json={'username': username,
                                                            'password': password,
                                                            'game_id': game_id})

                        # Check if the response contains valid JSON
                        try:
                            response_data = response.json()
                            print(response_data)
                            gotten_response = str(response_data['vysledek'])
                            print(gotten_response)

                            if gotten_response == "true" or gotten_response == "Uživatel již hru vlastní.":
                                self.owned = True
                                self.locked = False
                            #print("self.owned je možná true")
                        except json.JSONDecodeError:
                            #print("Error: Response is not valid JSON")
                            #print("Response content:", response.text)
                            return

                        vysledek = response_data.get('vysledek')


                    except requests.RequestException as e:
                        # Handle any requests exceptions
                        #print(f"An error occurred: {e}")
                        pass

                    check_balance = True
                    return check_balance
                    #TODO: aktualizování hodnoty money


def check_ownership(games_owned, games):
    for game in games:
        for number in games_owned:
            if number == game.id:
                game.owned = True
                game.locked = False



def get_games(games_owned):
    # sem vypisujte své hry ve formátu:
    # název hry, její popis, kolikátá je v pořadí (podle databáze, doptejte se), název její složky,
    # název hlavní funkce (pokud je), zda je defaultně uzamčená

    # lze se řídit vzorem pokerun, poté co napíšete ten jeden řádek tak její název přidejte do listu games,
    # který je na konci

    # takto dlouhý text je limit!
    # 72 characters
    # pokud je delší, vymysli si kratší, nebo uprav kód

    # na konec svého kódu umistěte tyto dva řádky
    # screen = pygame.display.set_mode((800, 800))
    # pygame.display.set_caption("EPLauncher")
    # toto takto dělejte dokud nezjistim jak to opravit

    # velikost pro ikony her je 55px * 55px
    # ikonu vložte do samé složky co máte hlavní soubor vaší hry a pojmenujte ji icon.png

    pokerun = Games("Pokérun", "Pokérun je skákací hra, ve které je hlavní cíl získat co nejvíce bodů.", 0, "Pokerun", "main", None, False, 0)
    sokobox = Games("Sokobox", "Sokobox je hra s cílem posunout všechny bedny na jejich určené místo.", 1000, "Sokobox", "Main", "Menu", True, 10)
    bageta = Games("Bageta", "Kupte si co nejlepší bagetu!", 1002, "bageta", "main", "automat", True, 0)
    flappybird = Games("Flappybird", "Dosáhněte co nejvyšího skóre!", 1001, "Flappy bird", "Flappy_Bird_py", "main", True, 0)

    # TODO: doplnit ID a cenu her (bageta, flappybird)
    games = [pokerun, sokobox, bageta, flappybird]

    check_ownership(games_owned, games)

    return games
