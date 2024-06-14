import pygame
import time
import random

pygame.init()

sirka, vyska = 800, 600
okno = pygame.display.set_mode((sirka, vyska))
pygame.display.set_caption("Speed Typing Test")

cervena = (255, 0, 0)
seda = (200, 200, 200)
bila = (255, 255, 255)
cerna = (0, 0, 0)

font = pygame.font.SysFont("Arial", 48)
medium_font = pygame.font.SysFont("verdana", 38)
small_font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Dosis", 38)

words = ["Na", "částice", "kapaliny", "působí", "v", "tíhovém", "poli", "země", "tíhová", "síla",
         "která", "se", "díky", "tekutosti", "přenáší", "na", "ostatní", "částice", "ve", "všech", "směrech", "a", "způsobuje",
         "hydrostatickou", "sílu", "saláti"]

words2 = ["V", "rovnovážné", "poloze", "jsou", "tělesa", "podepřená", "pod", "těžištěm", "nebo", "zavěšená",
          "nad", "těžištěm.", "Při", "vychílení", "tělesa", "z", "rovnovážné", "polohy", "se", "změní", "podmínky", "rovnováhy", "a",
          "přitom", "mohou", "nastat", "tři", "příklady", "saláti"]

def main():
    run = True
    input_text = ''
    word_index = 0
    start_time = 0
    game_over = False
    win = False
    elapsed_time = 0
    current_words = random.choice([words, words2])
    total_words = len(current_words)

    while run:
        okno.fill(bila)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if start_time == 0:
                        start_time = time.time()
                    
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

                    if input_text.strip() == current_words[word_index]:
                        word_index += 1
                        input_text = ''
                        
                        if word_index == total_words:
                            elapsed_time = time.time() - start_time
                            game_over = True
                            win = elapsed_time <= 50

        if not game_over and start_time != 0:
            elapsed_time = time.time() - start_time

        if game_over:
            if win:
                end_text = f"Vyhráli jste! Čas: {elapsed_time:.2f} sekund."
            else:
                end_text = f"Prohráli jste! Čas: {elapsed_time:.2f} sekund."
            
            end_surface = font.render(end_text, True, cerna)
            okno.blit(end_surface, (sirka // 2 - end_surface.get_width() // 2, vyska // 2 - end_surface.get_height() // 2))

            restart_text = "Stiskněte R pro restart nebo Q pro ukončení."
            restart_surface = small_font.render(restart_text, True, cerna)
            okno.blit(restart_surface, (sirka // 2 - restart_surface.get_width() // 2, vyska // 2 + end_surface.get_height()))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = False
                        input_text = ''
                        word_index = 0
                        start_time = 0
                        elapsed_time = 0
                        current_words = random.choice([words, words2]) 
                        total_words = len(current_words)
                    elif event.key == pygame.K_q:
                        run = False
        else:
            if word_index < total_words:
                current_word_surface = font.render(current_words[word_index], True, cerna)
                okno.blit(current_word_surface, (sirka // 2 - current_word_surface.get_width() // 2, vyska // 2 - current_word_surface.get_height() // 2))

            input_surface = font.render(input_text, True, cerna)
            okno.blit(input_surface, (sirka // 2 - input_surface.get_width() // 2, vyska // 2 + current_word_surface.get_height()))

            elapsed_time_text = f"Čas: {elapsed_time:.2f} s"
            elapsed_time_surface = medium_font.render(elapsed_time_text, True, cerna)
            okno.blit(elapsed_time_surface, (sirka // 2 - elapsed_time_surface.get_width() // 2, 10))
            
            goal_text = "Cíl: Napsat zápis z Fyziky za méně než 50 sekund."
            goal_surface = big_font.render(goal_text, True, cervena)
            okno.blit(goal_surface, (sirka // 2 - goal_surface.get_width() // 2, vyska - 80))

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
