import pygame
import pygame.freetype
import random
import time

pygame.init()
size = 1000, 600
screen = pygame.display.set_mode(size)
running = True
opravovani = False
rules = False
vyhra = False
hearts = 3
clock = pygame.time.Clock()


title = pygame.image.load("obrázky/opraf_chiby2.png")
title_rect = title.get_rect(center=(500, 150))
button = pygame.image.load("obrázky/hrat_button.png")
button_rect = button.get_rect(center=(500, 450))
pravidla = pygame.image.load("obrázky/pravidla.png")
pravidla_rect = pravidla.get_rect(center=(900, 550))
rules_cross = pygame.image.load("obrázky/rules_end.png")
rules_cross_rect = rules_cross.get_rect(center=(940, 50))
win = pygame.image.load("obrázky/vyhra.png")
win_rect = win.get_rect(center=(500, 250))
menu = pygame.image.load("obrázky/menu.png")
menu = pygame.transform.scale(menu, (200, 100))
menu_rect = menu.get_rect(center=(475, 535))

font = pygame.freetype.SysFont(None, 24)
sentences = [
    ("Kravata a zako mu skvěle ladili.", "Kravata a sako mu skvěle ladily."),
    ("Šelmi se živý drobnými živočichy.", "Šelmy se živí drobnými živočichy."),
    ("Její kosti odpočívaly v hrobě.", "Její kosti odpočívaly v hrobě."),
    ("Dědečkovy ubívaly síly.", "Dědečkovi ubývaly síly."),
    ("Rybízi z červenali.", "Rybízy zčervenaly."),
    ("Martina a magda bruslili.", "Martina a Magda bruslily."),
    ("Stébla trávy se vlnily ve vjetru.", "Stébla trávy se vlnila ve větru."),
    ("Legenda o Brumbálovy.", "Legenda o Brumbálovi."),
    ("Šváby jsou černý brouci.", "Švábi jsou černí brouci."),
    ("Okolnosti i lidé se zmněnily.", "Okolnosti i lidé se změnili."),
    ("Tisíce lidí se sešli na letné.", "Tisíce lidí se sešly na Letné."),
    ("Vidry lový ryby.", "Vydry loví ryby."),
    ("Jana šla do školi.", "Jana šla do školy."),
    ("Psy rychle běžely.", "Psi rychle běželi."),
    ("Z rána jsme se vydali na houby.", "Zrána jsme se vydali na houby."),
    ("Husté lesi skrývají datli.", "Husté lesy skrývají datly."),
    ("Herci, baletky i uvaděčky pracovali v divadle.", "Herci, baletky i uvaděčky pracovali v divadle."),
    ("V televizi vysílali pohádky.", "V televizi vysílali pohádky."),
]
correct_sentence = ""
current_sentence = ""
user_input = ''
input_rect = pygame.Rect(200, 300, 600, 50)
result_message = ''
result_color = (0, 0, 0)
total_correct = 0
max_sentences = 10

WHITE = (255, 255, 255)
LIGHT_BLUE = (235, 255, 255)
LIGHT_PINK = (255, 245, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

cursor_visible = True
cursor_time = 0

def draw_text(text, position, color=BLACK):
    font.render_to(screen, position, text, color)

def check_sentence():
    global result_message, result_color, total_correct, opravovani, vyhra, hearts
    if user_input == correct_sentence:
        result_message = "Správně! Opravil(a) jsi větu správně."
        result_color = GREEN
        total_correct += 1
        if total_correct >= max_sentences:
            opravovani = False
            vyhra = True
        else:
            next_sentence()
    else:
        result_message = "Špatně. Zkus to znovu."
        result_color = RED
        hearts -= 1
        if hearts == 0:
            opravovani = False
            
def shuffle_sentences():
    random.shuffle(sentences)

shuffle_sentences()

def next_sentence():
    global current_sentence, correct_sentence, user_input, result_message
    if len(sentences) > 0:
        current_sentence, correct_sentence = random.choice(sentences)
        sentences.remove((current_sentence, correct_sentence))
        user_input = ''
    else:
        current_sentence, correct_sentence = "", ""
        opravovani = False

while running:
    screen.fill(WHITE)
    if not opravovani and not rules and not vyhra:
        screen.blit(title, title_rect)
        screen.blit(button, button_rect)
        screen.blit(pravidla, pravidla_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not opravovani and not rules and not vyhra:
                if button_rect.collidepoint(event.pos):
                    opravovani = True
                    result_message = ''
                    total_correct = 0
                    hearts = 3
                    random.shuffle(sentences)
                    next_sentence()
                elif pravidla_rect.collidepoint(event.pos):
                    rules = True
            elif rules and rules_cross_rect.collidepoint(event.pos):
                rules = False
            elif vyhra and menu_rect.collidepoint(event.pos):
                vyhra = False
        elif event.type == pygame.KEYDOWN and opravovani:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                check_sentence()
            else:
                user_input += event.unicode

    if opravovani:
        screen.fill(LIGHT_BLUE)
        draw_text(f"Opravte tuto větu: '{current_sentence}'", (200, 250))
        pygame.draw.rect(screen, GRAY, input_rect, 2)
        text_surface, _ = font.render(user_input, BLACK)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 15))

        
        if cursor_visible:
            pygame.draw.line(screen, BLACK, (input_rect.x + 5 + text_surface.get_width(), input_rect.y + 10), (input_rect.x + 5 + text_surface.get_width(), input_rect.y + 40), 2)
        
        draw_text(f"Pro zkontrolování věty zmáčkni ENTER", (225, 360))
        draw_text(f"Opraveno {total_correct}/10 ", (800, 550))
        draw_text(f"Životy: {hearts} ", (50, 550))
        if result_message:
            draw_text(result_message, (200, 500), result_color)

        
        if pygame.time.get_ticks() - cursor_time > 500:
            cursor_visible = not cursor_visible
            cursor_time = pygame.time.get_ticks()

    if rules:
        screen.fill(LIGHT_PINK)
        screen.blit(rules_cross, rules_cross_rect)
        draw_text(f"Pravydla", (425, 50))
        draw_text(f"Oprav větu tak, že ji celou přepíšeš včetně diakritiky a velkých písmen.", (35, 100))
        draw_text(f"Opravuj tím, že napíšeš správnou větu na klávesnici.", (35, 160))
        draw_text(f"Dej si pozor, abys nedal mezeru za tečkou na konci, pak se to počítá jako špatně.", (35, 220))
        draw_text(f"Máš tři životy, takže se snaž, až opravíš 10 vět vyhráváš.", (35, 280))
        draw_text(f"Když přijdeš o všechny 3 životy, tvoje opravené věty se vynulují a začínáš od znova.", (35, 340))
        draw_text(f"Nepodváděj!", (35, 400))
        draw_text(f"A to hlavní: užij si hru <3", (35, 460))

    if vyhra:
        screen.fill((255, 255, 255))
        screen.blit(win, win_rect)
        screen.blit(menu, menu_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

