import pygame
import sys
import os
import random
import time

# ====================SokoBox==================
# Předloha hry je stará dobrá klasika arkádová hra SokoBan 
# Hra je součástí projektu "EP Launcher" od SPŠ Trutnov (1.EP) 2024
# Pro odemknutí achievementu je potřeba získat skóre 65 a více 
# =============================================

# Kontent herního okna
WIDTH = 780
HEIGHT = 600
TILE_SIZE = 60  # Upravitelné

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200,0,0)
GOLD = (255, 215, 0)
GREEN = (0,200,0)

# Skóre
elapsed_time = 0
moves = 0
counting = True
points = 0

# Class pro hráče
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join('minihry/Sokobox/source/Textures', 'player_texture.png')).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 'right'

    def rotate(self, direction):
        if direction == 'left':
            self.image = pygame.transform.flip(self.original_image, True, False)  # Flip horizontally for left
        elif direction == 'right':
            self.image = self.original_image
        self.direction = direction

# Class pro bedny
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('minihry/Sokobox/source/Textures', 'box_texture.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))

# Class pro zdi
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('minihry/Sokobox/source/Textures', 'wall_texture.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))

# Class pro umístění beden
class Spot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('minihry/Sokobox/source/Textures', 'box_place_texture.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))

# Definice levelů
level1 = [
    "########",
    "#      #",
    "# # BB #",
    "#P#S  S#",
    "########",
]

level2 = [
    "####    ",
    "#  #####",
    "# B#S#P#",
    "#  # # #",
    "#      #",
    "###  ###",
    "  ####  "
]

level3 = [
    " ####   ",
    " #P ### ",
    " # B  # ",
    "### # ##",
    "#S# #  #",
    "#S B # #",
    "#S   B #",
    "########",
]

level4 = [
    "  ####  ",
    "  #SS#  ",
    " ##  ## ",
    " # P S# ",
    "## B  ##",
    "#  #BB #",
    "#      #",
    "########"
]

level5 = [
    "#####    ",
    "#P  #    ",
    "# BB# ###",
    "# B # #S#",
    "### ###S#",
    " ##    S#",
    " #   #  #",
    " #   ####",
    " #####"
]

level6 = [
    " ###### ",
    " #    ##",
    "##S##B #",
    "# SSB  #",
    "#  #B  #",
    "#  P ###",
    "######"
]
# Funkce generování levelů
def generate_new_level(level_template):
    return level_template

def load_new_level(levels, level_index):
    if level_index < len(levels) - 1:  # Zkontroluje zda je nový level k dispozici
        level_index += 1
        # Generuje level
        return generate_new_level(levels[level_index])
    else:
        return None  # Vrátí nic, pokud nejsou další levely

# Funkce pro nakreslení/render levelu
def draw_level(level):
    all_sprites = pygame.sprite.LayeredUpdates()
    walls = pygame.sprite.Group()
    boxes = pygame.sprite.Group()
    player = None
    spots = pygame.sprite.Group()

    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == '#':
                wall = Wall(x * TILE_SIZE, y * TILE_SIZE)
                all_sprites.add(wall, layer=0)
                walls.add(wall)
            elif tile == 'P':
                player = Player(x * TILE_SIZE, y * TILE_SIZE)
                all_sprites.add(player, layer=1)
            elif tile == 'B':
                box = Box(x * TILE_SIZE, y * TILE_SIZE)
                all_sprites.add(box, layer=1)
                boxes.add(box)
            elif tile == "S":
                spot = Spot(x * TILE_SIZE, y * TILE_SIZE)
                spots.add(spot)

    # nastaví umístněním bened niší úroveň
    for spot in spots:
        all_sprites.add(spot, layer=0)

    return all_sprites, walls, boxes, player, spots

# Hlavní funkce
pygame.display.set_caption('SokoBox')
def hra():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    level_index = 0 
    levels = [level1, level2, level3, level4, level5, level6]

    all_sprites, walls, boxes, player, spots = draw_level(levels[level_index])

    start_time = pygame.time.get_ticks()

    running = True
    while running:
        global elapsed_time
        global counting
        global moves
        global points
        if counting:
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  
        
        moving = False  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif not all(box.rect.topleft == spot.rect.topleft for box in boxes for spot in spots):
                    if not moving:
                        new_x, new_y = player.rect.x, player.rect.y
                        if event.key == pygame.K_LEFT:
                            new_x -= TILE_SIZE
                            player.rotate('left')
                        elif event.key == pygame.K_RIGHT:
                            new_x += TILE_SIZE
                            player.rotate('right') 
                        elif event.key == pygame.K_UP:
                            new_y -= TILE_SIZE
                        elif event.key == pygame.K_DOWN:
                            new_y += TILE_SIZE
                        elif event.key == pygame.K_r:
                            all_sprites, walls, boxes, player, spots = draw_level(levels[level_index])
                        
                        # Zkontroluje zda je krok povolen v zájmu se stěnou
                        if not any(wall.rect.collidepoint(new_x, new_y) for wall in walls):
                            # Zkontroluje zda je před hráčem bedna
                            box_to_move = None
                            for box in boxes:
                                if box.rect.x == new_x and box.rect.y == new_y:
                                    box_to_move = box
                                    break
                            
                            # Pokud je Bedna zkontroluje místo před bednou
                            if box_to_move:
                                new_box_x, new_box_y = box_to_move.rect.x, box_to_move.rect.y
                                if event.key == pygame.K_LEFT:
                                    new_box_x -= TILE_SIZE
                                elif event.key == pygame.K_RIGHT:
                                    new_box_x += TILE_SIZE
                                elif event.key == pygame.K_UP:
                                    new_box_y -= TILE_SIZE
                                elif event.key == pygame.K_DOWN:
                                    new_box_y += TILE_SIZE
                                
                                # Pokud je místo před bednou
                                if not any(wall.rect.collidepoint(new_box_x, new_box_y) for wall in walls) \
                                    and not any(box.rect.collidepoint(new_box_x, new_box_y) for box in boxes):
                                    player.rect.x, player.rect.y = new_x, new_y
                                    box_to_move.rect.x, box_to_move.rect.y = new_box_x, new_box_y
                                    moving = True
                                    moves += 1
                            else:
                                player.rect.x, player.rect.y = new_x, new_y
                                moving = True
                                moves += 1

        # Check if all boxes are on their spots
        all_boxes_on_spots = all(any(box.rect.topleft == spot.rect.topleft for spot in spots) for box in boxes)
        
        screen.fill((17, 1, 63))
        all_sprites.draw(screen)
        
        font = pygame.font.Font(None, 40)
        time_text = font.render(f"Time: {elapsed_time}s", True, WHITE) 
        time_rect = time_text.get_rect(center=(650, 60))
        screen.blit(time_text, time_rect)
        
        font = pygame.font.Font(None, 40)
        time_text = font.render(f"Moves: {moves}x", True, WHITE)
        time_rect = time_text.get_rect(center=(650, 20))
        screen.blit(time_text, time_rect)
        
        font = pygame.font.Font(None, 20)
        time_text = font.render("´R´ for reset level", True, RED)
        time_rect = time_text.get_rect(center=(60, 590))
        screen.blit(time_text, time_rect)

        if all_boxes_on_spots:
            if level_index < len(levels) - 1: 
                level_index += 1
                # Vygeneruje nový level
                all_sprites, walls, boxes, player, spots = draw_level(levels[level_index])
            else:
                font = pygame.font.Font(None, 55)
                text = font.render(f"You completed all levels! Score: {points}", True, GOLD)
                text_rect = text.get_rect(center=(WIDTH // 2, 490))
                screen.blit(text, text_rect)
                if counting:
                    print("Moves:", moves, "Time:", elapsed_time, "Level:", level_index)
                    if moves < 330:
                        points += 8
                    elif moves >= 330 and moves < 345:
                        points += 5
                    elif moves >= 345:
                        points -= 1
                    if elapsed_time < 90:
                        points += 15
                    elif elapsed_time >= 90 and elapsed_time < 100:
                        points += 9
                    elif elapsed_time >= 100 and elapsed_time < 115:
                        points += 2
                    elif elapsed_time >= 115:
                        points -= 1
                    points += level_index * 10
                    print("Points:", points)
                    counting = False
                    
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    sys.exit()
    
    if points >= 70:
        return True, "Sokobox speedrun GOD!"
    
    
def Menu():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill((17, 1, 63))
        font = pygame.font.Font(None, 100)
        text = font.render("SokoBox", True, WHITE)
        rect = text.get_rect(center=(370, 100))
        screen.blit(text, rect)
        text_play = font.render("PLAY", True, GREEN)
        rect_play = text_play.get_rect(center=(370,380))
        screen.blit(text_play, rect_play)
        m_state = pygame.mouse.get_pressed()
        m_pos = pygame.mouse.get_pos()
        if m_state[0] and rect_play.collidepoint(m_pos):
            hra()
            running = False 
            break 
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()
    return points

Menu()
