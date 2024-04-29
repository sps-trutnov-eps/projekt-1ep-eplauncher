import pygame
import sys

# Nastavení velikosti okna
WIDTH = 800
HEIGHT = 600

# Nastavení barev
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Třída pro hráčovu postavu
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('player_texture.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

# Třída pro bedny
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('box_texture.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

# Třída pro stěny
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('wall_texture.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

# Inicializace Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Vytvoření hráčovy postavy, beden a stěn
player = Player(50, 50)
box = Box(150, 150)
wall = Wall(250, 250)

# Skupina spritů pro snadnější manipulaci s objekty
all_sprites = pygame.sprite.Group()
all_sprites.add(player, box, wall)

# Hlavní smyčka hry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Pohyb hráče pomocí šipek
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    elif keys[pygame.K_RIGHT]:
        player.rect.x += 5
    elif keys[pygame.K_UP]:
        player.rect.y -= 5
    elif keys[pygame.K_DOWN]:
        player.rect.y += 5

    # Vyplnění obrazovky bílou barvou
    screen.fill(WHITE)
    # Vykreslení všech spritů
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
