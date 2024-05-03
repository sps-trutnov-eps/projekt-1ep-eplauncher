import pygame
import sys
import os
import random

# Constants for colors and sizes
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 40  # Adjusted to 40x40 for 2 times bigger textures

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Class for the player character
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('Textures', 'player_texture.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))

# Class for boxes
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('Textures', 'box_texture.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))

# Class for walls
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('Textures', 'wall_texture.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))

# Class for box spot
class Spot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('Textures', 'box_place_texture.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))

# Function to generate random level layout
def generate_level():
    level = [
        "########",
        "#      #",
        "# # BB #",
        "#P#S  S#",
        "########",
    ]
    return level

# Function to draw the level
def draw_level(level):
    all_sprites = pygame.sprite.LayeredUpdates()  # Use LayeredUpdates for layer management
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

    # Add spots to all_sprites with a lower layer than boxes
    for spot in spots:
        all_sprites.add(spot, layer=0)  # Set layer to 0 (lower layer)

    return all_sprites, walls, boxes, player, spots

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    level = generate_level()
    all_sprites, walls, boxes, player, spots = draw_level(level)

    running = True
    while running:
        moving = False  # Reset moving flag before each iteration
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif not all(box.rect.topleft == spot.rect.topleft for box, spot in zip(boxes, spots)):
                    # Allow player to move only if not all boxes are on spots
                    if not moving:  # If not already moving
                        # Calculate the new position the player wants to move to
                        new_x, new_y = player.rect.x, player.rect.y
                        if event.key == pygame.K_LEFT:
                            new_x -= TILE_SIZE
                        elif event.key == pygame.K_RIGHT:
                            new_x += TILE_SIZE
                        elif event.key == pygame.K_UP:
                            new_y -= TILE_SIZE
                        elif event.key == pygame.K_DOWN:
                            new_y += TILE_SIZE
                        
                        # Check if the new position is obstructed by a wall
                        if not any(wall.rect.collidepoint(new_x, new_y) for wall in walls):
                            # Check if there is a box in the new position
                            box_to_move = None
                            for box in boxes:
                                if box.rect.x == new_x and box.rect.y == new_y:
                                    box_to_move = box
                                    break
                            
                            # If there is a box, check if the space beyond it is empty
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
                                
                                # Check if the space beyond the box is empty
                                if not any(wall.rect.collidepoint(new_box_x, new_box_y) for wall in walls) \
                                    and not any(box.rect.collidepoint(new_box_x, new_box_y) for box in boxes):
                                    # Move both player and box
                                    player.rect.x, player.rect.y = new_x, new_y
                                    box_to_move.rect.x, box_to_move.rect.y = new_box_x, new_box_y
                                    moving = True  # Set moving flag to True
                            else:
                                # Move the player only if there is no box in the new position
                                player.rect.x, player.rect.y = new_x, new_y
                                moving = True  # Set moving flag to True

        # Check if all boxes are on spots
        all_boxes_on_spots = all(box.rect.topleft == spot.rect.topleft for box, spot in zip(boxes, spots))

        screen.fill(WHITE)
        # Draw all sprites
        all_sprites.draw(screen)
        
        if all_boxes_on_spots:
            font = pygame.font.Font(None, 36)
            text = font.render("Congratulations! All boxes are on spots!", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
