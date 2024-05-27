import pygame
import pygame.freetype
import random

pygame.init()
size = 1000, 600
screen = pygame.display.set_mode(size)
running = True
opravovani = False
rules = False
vyhra = False
clock = pygame.time.Clock()

# Load images
title = pygame.image.load("obrázky/opraf_chiby2.png")
title_rect = title.get_rect(center=(500, 150))
button = pygame.image.load("obrázky/hrat_button.png")
button_rect = button.get_rect(center=(500, 450))
pravidla = pygame.image.load("obrázky/pravidla.png")
pravidla_rect = pravidla.get_rect(center=(900, 550))
rules_cross = pygame.image.load("obrázky/rules_end.png")
rules_cross_rect = rules_cross.get_rect(center=(940, 50))

# Font setup
font = pygame.freetype.SysFont(None, 24)
sentences = [
	("Kravata a zako mu skvěle ladili.", "Kravata a sako mu skvěle ladily."),
	("Šelmi se živý drobnými živočichy.", "Šelmy se živí drobnými živočichy."),
	("Její kosti odpočívaly v hrobě.", "Její kosti odpočívaly v hrobě."),
	("Dědečkovy ubívaly síly.", "Dědečkovi ubývaly síly."),
	("Rybízi z červenali.", "Rybízy zčervenaly."),
	("Martina a magda bruslej.", "Martina a Magda bruslí."),
	("Stébla trávy se vlnily ve vjetru.", "Stébla trávy se vlnila ve větru."),
	("Legenda o Brumbálovy.", "Legenda o Brumbálovi"),
	("Šváby jsou černý brouci.", "Švábi jsou černí brouci."),
	("Okolnosti i lidé se zmněnily.", "Okolnosti i lidé se změnili."),
	("Tisíce lidí se sešli na letné.", "Tisíce lidí se sešly na Letné."),
	("Vidry lový ryby.", "Vydry loví ryby."),
	("Jana šla do školi.", "Jana šla do školy."),
	("Psy běžely rychle.", "Psi běželi rychle."),
	("To auto je můj.", "To auto je moje."),
	("Oni byly unavený.", "Oni byli unavení."),
	("Moje oblíbená barva je modrý.", "Moje oblíbená barva je modrá."),
	("Z rána jsme se vydaly na houby.", "Zrána jsme se vydali na houby."),
	("Husté lesi skrývají datli.", "Husté lesy skrývají datly."),
	("Herci, baletky i uvaděčky pracovali v divadle.", "Herci, baletky i uvaděčky pracovali v divadle."),
	("V televizi vysílali pohádky.", "V televizi vysílali pohádky."),
]
correct_sentence = ""
current_sentence = ""
user_input = ''
input_rect = pygame.Rect(200, 300, 600, 50)
check_button_rect = pygame.Rect(425, 400, 150, 50)
result_message = ''
result_color = (0, 0, 0)
total_correct = 0
max_sentences = 1

# Colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (235, 255, 255)
LIGHT_PINK = (255, 245, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_text(text, position, color=BLACK):
	font.render_to(screen, position, text, color)

def check_sentence():
	global result_message, result_color, total_correct, opravovani
	if user_input == correct_sentence:
		result_message = "Správně! Opravil(a) jsi větu správně."
		result_color = GREEN
		total_correct += 1
		if total_correct >= max_sentences:
			result_message = "Vyhrál(a) jsi! Opravil(a) jsi všechny věty správně."
			opravovani = False
		else:
			next_sentence()
	else:
		result_message = "Špatně. Zkus to znovu."
		result_color = RED

def next_sentence():
	global current_sentence, correct_sentence, user_input, result_message, vyhra
	if len(sentences) > 0:
		current_sentence, correct_sentence = random.choice(sentences)
		sentences.remove((current_sentence, correct_sentence))
		user_input = ''
	else:
		current_sentence, correct_sentence = "", ""
		result_message = "Žádné další věty nejsou k dispozici."
		opravovani = False
		vyhra = True

while running:
	screen.fill(WHITE)
	screen.blit(title, title_rect)
	screen.blit(button, button_rect)
	screen.blit(pravidla, pravidla_rect)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if button_rect.collidepoint(event.pos):
				opravovani = True
				result_message = ''
				total_correct = 0
				random.shuffle(sentences)
				next_sentence()
			elif pravidla_rect.collidepoint(event.pos):
				rules = True 
			elif rules_cross_rect.collidepoint(event.pos):
				rules = False
			elif check_button_rect.collidepoint(event.pos) and opravovani:
				check_sentence()
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
		draw_text(user_input, (input_rect.x + 5, input_rect.y + 15))
		draw_text(f"Pro zkontrolování věty zmáčkni ENTER", (225, 360))
		if result_message:
			draw_text(result_message, (200, 500), result_color)
	
	if rules:
		screen.fill(LIGHT_PINK)
		screen.blit(rules_cross, rules_cross_rect)
	if vyhra:
		screen.fill((255,255,255))
		
	pygame.display.update()
	clock.tick(60)

pygame.quit()

