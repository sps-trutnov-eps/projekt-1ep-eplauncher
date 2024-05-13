import pygame
import sys
import os
import random

# Constants for colors and sizes
WIDTH = 780
HEIGHT = 600
TILE_SIZE = 60  # Adjusted

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200,0,0)
GOLD = (255, 215, 0)

# Score
elapsed_time = 0
moves = 0
counting = True
points = 0

# Class for the player character
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join('Textures', 'player_texture.png')).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (TILE_SIZE, TILE_SIZE))  # Resize image
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 'right'  # Initial direction is right

    def rotate(self, direction):
        if direction == 'left':
            self.image = pygame.transform.flip(self.original_image, True, False)  # Flip horizontally for left
        elif direction == 'right':
            self.image = self.original_image
        self.direction = direction

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

# Define level templates
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
    "#    # #",
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
    "#  B# ###",
    "# B # #S#",
    "### ###S#",
    " ##     #",
    " #   #  #",
    " #   ####",
    " #####",
]

# Function to generate a new level
def generate_new_level(level_template):
    return level_template

def load_new_level(levels, level_index):
    if level_index < len(levels) - 1:  # Check if there are more levels
        level_index += 1
        # Generate next level
        return generate_new_level(levels[level_index])
    else:
        return None  # Return None if there are no more levels

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
pygame.display.set_caption('SokoBox')
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    level_index = 0  # Keep track of the current level index
    levels = [level1, level2, level3, level4, level5]  # Define specific level templates

    all_sprites, walls, boxes, player, spots = draw_level(levels[level_index])

    start_time = pygame.time.get_ticks()  # Get the initial time

    running = True
    while running:
        global elapsed_time
        global counting
        global moves
        global points
        if counting:
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Calculate elapsed time in seconds
        
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
                            player.rotate('left')  # Rotate the player left
                        elif event.key == pygame.K_RIGHT:
                            new_x += TILE_SIZE
                            player.rotate('right')  # Rotate the player right
                        elif event.key == pygame.K_UP:
                            new_y -= TILE_SIZE
                        elif event.key == pygame.K_DOWN:
                            new_y += TILE_SIZE
                        elif event.key == pygame.K_r:
                            # Restart level
                            all_sprites, walls, boxes, player, spots = draw_level(levels[level_index])
                        
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
                                    moves += 1
                            else:
                                # Move the player only if there is no box in the new position
                                player.rect.x, player.rect.y = new_x, new_y
                                moving = True  # Set moving flag to True
                                moves += 1

        # Check if all boxes are on spots
        all_boxes_on_spots = all(box.rect.topleft == spot.rect.topleft for box, spot in zip(boxes, spots))

        screen.fill((17, 1, 63))
        # Draw all sprites
        all_sprites.draw(screen)
        
        font = pygame.font.Font(None, 40)
        time_text = font.render(f"Time: {elapsed_time}s", True, WHITE)  # Render text with elapsed time
        time_rect = time_text.get_rect(center=(650, 60))
        screen.blit(time_text, time_rect)
        
        font = pygame.font.Font(None, 40)
        time_text = font.render(f"Moves: {moves}x", True, WHITE)  # Render text with elapsed time
        time_rect = time_text.get_rect(center=(650, 20))
        screen.blit(time_text, time_rect)
        
        font = pygame.font.Font(None, 20)
        time_text = font.render("´R´ for reset level", True, RED)  # Render text with elapsed time
        time_rect = time_text.get_rect(center=(60, 590))
        screen.blit(time_text, time_rect)
        if all_boxes_on_spots:
            if level_index < len(levels) - 1:  # Check if there are more levels
                level_index += 1
                # Generate next level
                all_sprites, walls, boxes, player, spots = draw_level(levels[level_index])
            else:
                font = pygame.font.Font(None, 65)
                text = font.render("You completed all levels!", True, GOLD)
                text_rect = text.get_rect(center=(WIDTH // 1.6, 560))
                screen.blit(text, text_rect)
                if counting:
                    print("Moves:",moves,"","Time:",elapsed_time,"","Level:",level_index)
                    if moves < 105:
                        points += 5
                    elif moves >= 105 and moves < 115:
                        points += 2
                    elif moves >= 115:
                        points -= 1
                    if elapsed_time < 40:
                        points += 5
                    elif elapsed_time >= 40 and moves < 50:
                        points += 2
                    elif elapsed_time >= 50:
                        points -= 1
                    print("Points:",points)
                    counting = False
                
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
