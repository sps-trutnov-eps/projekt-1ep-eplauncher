import pygame
import random
import time


pygame.init()


sirka, vyska = 800, 600
window = pygame.display.set_mode((sirka, vyska))
pygame.display.set_caption("Speed Typing Test")


bila = (255, 255, 255)
cerna = (0, 0, 0)


font = pygame.font.SysFont("Arial", 48)
small_font = pygame.font.SysFont("Arial", 24)


words = ["kočka", "pes", "stůl", "židle", "auto", "kolo", "čas", "den", "noc", "týden","měsíc", "rok", "voda", "vítr", "mrak", "slunce", "město", "vesnice", "les","hora", "řeka", "potok", "moře", "ocean", "strom", "kvetina", "tráva", "země","svět", "světlo", "stín", "krása", "radost", "smutek", "láska", "náklonnost","soucit", "nádech", "výdech", "pohyb", "klid", "základ", "záměr", "cíl", "plán","dům", "chata", "bytek", "pohovka", "postel", "matrace", "polštář", "koberec","okno", "dveře", "střecha", "zeď", "podlaha", "schody", "koupelna", "kuchyně","obývací", "pokoj", "ložnice", "garáž", "záhrada", "skleník", "plot", "brána","práce", "úkol", "plán", "projekt", "cíl", "úspěch", "neúspěch", "výsledek","zkušenost", "znalost", "dojmy", "pocity", "nálada", "atmosféra", "veselí","klid", "radost", "vítězství", "porážka", "soutěž", "turnaj", "úcta", "sláva"]
total_words = 100

def get_random_words(n):
    return [random.choice(words) for _ in range(n)]

def main():
    run = True
    input_text = ''
    word_list = get_random_words(total_words)
    word_index = 0
    start_time = 0
    completed_words = 0
    wpm = 0
    game_over = False

    while run:
        window.fill(bila)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if start_time == 0:
                    start_time = time.time()

                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

                if input_text.strip() == word_list[word_index]:
                    completed_words += 1
                    word_index += 1
                    input_text = ''

                    if word_index == total_words:
                        word_list = get_random_words(total_words)
                        word_index = 0

        if start_time != 0:
            elapsed_time = time.time() - start_time
            wpm = (completed_words / elapsed_time) * 60 if elapsed_time > 0 else 0

            if wpm >= 50:
                game_over = True

        if game_over:
            end_text = "Konec hry! Dosáhli jste 50 WPM."
            end_surface = font.render(end_text, True, cerna)
            window.blit(end_surface, (sirka // 2 - end_surface.get_width() // 2, vyska // 2 - end_surface.get_height() // 2))

            restart_text = "Stiskněte R pro restart nebo Q pro ukončení."
            restart_surface = small_font.render(restart_text, True, cerna)
            window.blit(restart_surface, (sirka // 2 - restart_surface.get_width() // 2, vyska // 2 + end_surface.get_height()))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = False
                        input_text = ''
                        word_list = get_random_words(total_words)
                        word_index = 0
                        start_time = 0
                        completed_words = 0
                        wpm = 0
                    elif event.key == pygame.K_q:
                        run = False
        else:
            current_word_surface = font.render(word_list[word_index], True, cerna)
            window.blit(current_word_surface, (sirka // 2 - current_word_surface.get_width() // 2, vyska // 2 - current_word_surface.get_height() // 2))

            input_surface = font.render(input_text, True, cerna)
            window.blit(input_surface, (sirka // 2 - input_surface.get_width() // 2, vyska // 2 + current_word_surface.get_height()))

            wpm_text = f"WPM: {wpm:.2f}"
            wpm_surface = small_font.render(wpm_text, True, cerna)
            window.blit(wpm_surface, (10, 10))

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
