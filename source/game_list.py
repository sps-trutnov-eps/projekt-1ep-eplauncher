class Games:
    def __init__(self, jmeno_hry, popis_hry, cislo_hry, nazev_slozky):
        self.name = jmeno_hry
        self.description = popis_hry
        self.id = cislo_hry
        self.location = nazev_slozky


Games("Pokérun", "Pokérun je hra, ve které je hlavní cíl získat co nejvíce bodů.", 1, "Pokerun")