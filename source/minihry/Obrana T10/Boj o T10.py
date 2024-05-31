import sys
import pygame
import random

pygame.init()

rozliseni_okna = (1500, 768)
okno = pygame.display.set_mode(rozliseni_okna)

# Definování barev a počátečního množství peněz
zluta = (255, 215, 0)
penize = 100
cena_kytka = 50
cena_strilec = 50
cena_zed = 100

# Načtení fontů
font = pygame.font.SysFont(None, 50)
font_cena = pygame.font.SysFont(None, 30)

# Inicializace časovače a hodin
casovac = pygame.time.get_ticks()
cas = pygame.time.Clock()
interval_pricteni_penez = 4000  # 4000 ms = 4 sekundy

# Nastavení odpočítávání času
zacatek_cas = 10 * 60  # 10 minut v sekundách
cas_aktualni = zacatek_cas
casovac_odpocet = pygame.time.get_ticks()

# Definování herní mřížky
herni_ctverce = [pygame.Rect(150 * i, 192 * j, 150, 192) for i in range(8) for j in range(4)]

# Načtení obrázků
kytka = pygame.image.load('kytka.png')
strilec = pygame.image.load('strilec.png')
zed = pygame.image.load('zed.png')
basic_nepritel = pygame.image.load('nepritel_basic.png')

kytka_rect = kytka.get_rect()
strilec_rect = strilec.get_rect()
zed_rect = zed.get_rect()
basic_nepritel_rect = basic_nepritel.get_rect()

# Definování proměnné pro vybraný objekt (None znamená, že žádný objekt není vybraný)
vybrany_objekt = None

# Vytvoření slovníku pro sledování umístěných objektů
umistene_objekty = {}

# Slovník pro sledování nepřátel a jejich počtu zásahů
nepratele = []
nepratele_zasahy = []

strely = []

def spawn_enemy():
    rada = random.randint(0, 3)
    x = rozliseni_okna[0] - basic_nepritel_rect.width - 150
    y = 192 * rada + (192 - basic_nepritel_rect.height) // 2
    nepratele.append(pygame.Rect(x, y, basic_nepritel_rect.width, basic_nepritel_rect.height))
    nepratele_zasahy.append(0)

spawn_timer = pygame.time.get_ticks()
spawn_interval = 6000     # 5000 = 5 sekund

class Strela:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 5)
        
    def move(self):
        self.rect.x += 5
        
    def draw(self, surface):
        pygame.draw.rect(surface, zluta, self.rect)

strilec_timer = pygame.time.get_ticks()
strilec_interval = 3000  # 1000 ms = 1 sekunda

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif udalost.type == pygame.MOUSEBUTTONDOWN:
            pozice = pygame.mouse.get_pos()
            for i, ctverec in enumerate(herni_ctverce):
                if ctverec.collidepoint(pozice):
                    if vybrany_objekt == 'kytka' and penize >= cena_kytka:
                        penize -= cena_kytka
                        umistene_objekty[i] = 'kytka'
                    elif vybrany_objekt == 'strilec' and penize >= cena_strilec:
                        penize -= cena_strilec
                        umistene_objekty[i] = 'strilec'
                    elif vybrany_objekt == 'zed' and penize >= cena_zed:
                        penize -= cena_zed
                        umistene_objekty[i] = 'zed'
                    print(f"Kliknuto na čtverec č.{i}, umístěno {vybrany_objekt}")

        elif udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_q:
                vybrany_objekt = 'kytka'
            elif udalost.key == pygame.K_w:
                vybrany_objekt = 'strilec'
            elif udalost.key == pygame.K_e:
                vybrany_objekt = 'zed'
            print(f"Vybraný objekt: {vybrany_objekt}")

    # Přičítání peněz periodicky
    casovac2 = pygame.time.get_ticks()
    if casovac2 - casovac > interval_pricteni_penez:
        penize += 20
        casovac = casovac2

    # Odpočítávání času
    casovac_odpocet2 = pygame.time.get_ticks()
    if casovac_odpocet2 - casovac_odpocet >= 1000:  # Každá vteřina
        cas_aktualni -= 1
        casovac_odpocet = casovac_odpocet2

    # Převod aktuálního času na formát mm:ss
    minuty = cas_aktualni // 60
    vteriny = cas_aktualni % 60
    cas_text = f"{minuty:02}:{vteriny:02}"

    # Konec hry, pokud čas dosáhne nuly
    if cas_aktualni <= 0:
        print("Konec hry! Třída byla obráněna a učitel nezačal hodinu!!!.")
        pygame.quit()
        sys.exit()

    # Spawn nového nepřítele každých 5 sekund
    if pygame.time.get_ticks() - spawn_timer > spawn_interval:
        spawn_enemy()
        spawn_timer = pygame.time.get_ticks()
        
    # Pohyb nepřátel
    for nepritel in nepratele:
        nepritel.x -= 0.9  # rychlost pohybu nepratel
        
    for nepritel in nepratele:
        if nepritel.x <= 0:
            pygame.quit()
            print("Učitel začal hodinu a celá třída se teď musí učit, určitě nebudou rádi!!!")
    # Vytvoření střel pro každého střílece
    current_time = pygame.time.get_ticks()
    if current_time - strilec_timer > strilec_interval:
        for i, obj in umistene_objekty.items():
            if obj == 'strilec':
                x = herni_ctverce[i].x + strilec_rect.width + 10 // 2
                y = herni_ctverce[i].y + (herni_ctverce[i].height - 5) // 2
                strely.append(Strela(x, y))
        strilec_timer = current_time
            
    # Pohyb střel
    for strela in strely:
        strela.move()
        
    # Odstranění střel mimo obrazovku a zásah nepřátel
    nove_strely = []
    for strela in strely:
        zasah = False
        for i, nepritel in enumerate(nepratele):
            if strela.rect.colliderect(nepritel):
                nepratele_zasahy[i] += 1
                zasah = True
                if nepratele_zasahy[i] >= 3:
                    nepratele.pop(i)
                    nepratele_zasahy.pop(i)
                    penize += 20                          # pricitani penez za kil
                break
        if not zasah and strela.rect.x < rozliseni_okna[0] - 180:
            nove_strely.append(strela)
    strely = nove_strely
    
    # Vykreslení pozadí a prvků uživatelského rozhraní
    okno.fill((34,139,34))
    penize_text = font.render(str(penize), True, zluta)
    cena_kytka_text = font_cena.render(f"{cena_kytka} - Q", True, zluta)
    cena_strilec_text = font_cena.render(f"{cena_strilec} - W", True, zluta)
    cena_zed_text = font_cena.render(f"{cena_zed} - E", True, zluta)
    cas_text_render = font.render(cas_text, True, zluta)

    pygame.draw.rect(okno, (255, 255, 255), (0, 192, 1320, 1))
    pygame.draw.rect(okno, (255, 255, 255), (0, 192*2, 1320, 1))
    pygame.draw.rect(okno, (255, 255, 255), (0, 192*3, 1320, 1))
    pygame.draw.rect(okno, (0, 0, 0), (150, 0, 1, 768))
    pygame.draw.rect(okno, (0, 0, 0), (150*2, 0, 1, 768))
    pygame.draw.rect(okno, (0, 0, 0), (150*3, 0, 1, 768))
    pygame.draw.rect(okno, (0, 0, 0), (150*4, 0, 1, 768))
    pygame.draw.rect(okno, (0, 0, 0), (150*5, 0, 1, 768))
    pygame.draw.rect(okno, (0, 0, 0), (150*6, 0, 1, 768))
    pygame.draw.rect(okno, (0, 0, 0), (150*7, 0, 1, 768))
    pygame.draw.rect(okno, (0, 0, 0), (150*8, 0, 1, 768))
    pygame.draw.rect(okno, (139, 69, 19), (1320, 0, 180, 768))
    pygame.draw.rect(okno, (0, 0, 0), (1320, 50, 180, 1))
    okno.blit(penize_text, (1320, 20))
    okno.blit(cas_text_render, (10, 10))
    okno.blit(kytka, (1360, 60))
    okno.blit(cena_kytka_text, (1390, 150))
    okno.blit(strilec, (1360, 210))
    okno.blit(cena_strilec_text, (1380, 310))
    okno.blit(zed, (1365, 360))
    okno.blit(cena_zed_text, (1380, 465))

    pygame.draw.rect(okno, (0, 0, 0), (1320, 200, 300, 1))
    pygame.draw.rect(okno, (0, 0, 0), (1320, 350, 300, 1))
    pygame.draw.rect(okno, (0, 0, 0), (1320, 500, 300, 1))
    pygame.draw.rect(okno, (0, 0, 0), (1320, 0, 1, 500))

    # Vykreslení umístěných objektů
    for i, obj in umistene_objekty.items():
        x, y = herni_ctverce[i].center
        if obj == 'kytka':
            x -= kytka_rect.width // 2
            y -= kytka_rect.height // 2
            okno.blit(kytka, (x, y))
        elif obj == 'strilec':
            x -= strilec_rect.width // 2
            y -= strilec_rect.height // 2
            okno.blit(strilec, (x, y))
        elif obj == 'zed':
            x -= zed_rect.width // 2
            y -= zed_rect.height // 2
            okno.blit(zed, (x, y))
    
    for nepritel in nepratele:
        okno.blit(basic_nepritel, nepritel.topleft)
    
    for strela in strely:
        strela.draw(okno)
    
    pygame.display.update()
    cas.tick(30)
