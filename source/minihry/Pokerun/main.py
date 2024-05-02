import pygame
from sys import exit
from random import randint, choice


class Hrac(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hrac = pygame.image.load("minihry/Pokerun/Files/hrac.png")
        self.hrac_skok = pygame.image.load("minihry/Pokerun/Files/skok.png")
        self.image = self.hrac
        self.rect = self.hrac.get_rect(midbottom = (100,300))
        self.gravity = 0
    def hrac_input(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

        if self.rect.bottom < 300:
            self.image = self.hrac_skok
        elif self.rect.bottom == 300:
            self.image = self.hrac
    def gravitace(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def update(self):
        self.hrac_input()
        self.gravitace()

class Prekazky(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "Pokemon1":
            Pokemon1 = pygame.image.load("minihry/Pokerun/Files/angry_anton.png")
            Pokemon1b = pygame.image.load("minihry/Pokerun/Files/run_angry_anton.png")
            self.pict = [Pokemon1, Pokemon1b]
            y_pos = 300
        else:
            Pokemon2 = pygame.image.load("minihry/Pokerun/Files/redbird.png")
            Pokemon2b = pygame.image.load("minihry/Pokerun/Files/rotflugzeug.png")
            self.pict = [Pokemon2, Pokemon2b]
            y_pos = 200
        self.animation = 0
        self.image = self.pict[self.animation]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))

    def animation_prekazky(self):
        self.animation += 0.05
        if self.animation >= len(self.pict):
            self.animation = 0
        self.image = self.pict[int(self.animation)]


    def update(self):
        self.animation_prekazky()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def collisions():
    global hearts
    if pygame.sprite.spritecollide(hrac.sprite, prekazky_group, True):
        hearts -= 1
        if hearts > 0:
            return True
        else:
            return False
    else: return True

def show_score():
    global bscore, final_score
    cas = int(pygame.time.get_ticks() / 1000) - start_time
    bonus_collision = pygame.sprite.spritecollide(hrac.sprite, bonus_group, True)
    if bonus_collision:
        bscore += 5
    final_score = cas + bscore


    score_surf = font.render(f"Score: {final_score}", False, (60,60,60))
    score_rect = score_surf.get_rect(center = (400, 55))
    screen.blit(score_surf, score_rect)
    return final_score

class Bonus(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "Bonus1":
            bonus_image1 = pygame.image.load("minihry/Pokerun/Files/Anton.png")
            bonus_image1b = pygame.image.load("minihry/Pokerun/Files/running_anton.png")
            self.pict = [bonus_image1, bonus_image1b]
            y_pos = 300
        else:
            bonus_image2 = pygame.image.load("minihry/Pokerun/Files/greenbird.png")
            bonus_image2b = pygame.image.load("minihry/Pokerun/Files/flugzeug.png")
            self.pict = [bonus_image2, bonus_image2b]
            y_pos = 200
        self.animation = 0
        self.image = self.pict[self.animation]
        self.rect = self.image.get_rect(midbottom=(randint(900,1100), y_pos))
    def animation_bonus(self):
        self.animation += 0.05
        if self.animation >= len(self.pict):
            self.animation = 0
        self.image = self.pict[int(self.animation)]

    def update(self):
        self.animation_bonus()
        self.rect.x -=6
        self.destroy()
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Pokérun")
clock = pygame.time.Clock()
hra = False
start_time = 0
final_score = 0
bscore = 0

hearts = 3

hrac = pygame.sprite.GroupSingle()
hrac.add(Hrac())
prekazky_group = pygame.sprite.Group()

bonus_group = pygame.sprite.Group()
bonus_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bonus_timer, randint(5000, 10000))

#files
obloha = pygame.image.load("minihry/Pokerun/Files/city_.png")
zeme = pygame.image.load("minihry/Pokerun/Files/ground.png")

font = pygame.font.Font(None, 44)
instruction = font.render("Stiskni [a] pro vstup do hry", False, (0, 30, 150))
instruction_rect = instruction.get_rect(center=(400, 75))
instruction2 = font.render("Stiskni [a] pro novou hru", False, (0, 30, 150))
instruction2_rect = instruction.get_rect(center=(420, 330))

prekazky_timer = pygame.USEREVENT + 1
pygame.time.set_timer(prekazky_timer, 1500)

game_running = True
while game_running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_running = False
            screen = pygame.display.set_mode((800, 800))
            pygame.display.set_caption("EPLauncher")
            hra = False

        if hra:
            if event.type == prekazky_timer:
                prekazky_group.add(Prekazky(choice(["Pokemon1","Pokemon1","Pokemon1","Pokemon2"])))
            elif event.type == bonus_timer:
                bonus_group.add(Bonus(choice(["Bonus1","Bonus1","Bonus2","Bonus2"])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                hra = True
                start_time = int(pygame.time.get_ticks() / 1000)
                final_score = 0
                bscore = 0
                hearts = 3
                prekazky_group.empty()
                bonus_group.empty()

    if hra:
        screen.blit(obloha, (0, 0))
        screen.blit(zeme, (0, 300))
        show_score()
        hearts_surf = font.render(f"Životy: {hearts}", False, (159,252,253))
        hearts_rect = hearts_surf.get_rect(center=(700, 365))
        screen.blit(hearts_surf, hearts_rect)
        hrac.draw(screen)
        hrac.update()

        prekazky_group.draw(screen)
        prekazky_group.update()

        #bonus_collision = pygame.sprite.spritecollide(hrac.sprite, bonus_group, True)
        bonus_group.draw(screen)
        bonus_group.update()
        hra = collisions()

    else:
        screen.fill((159, 252, 253))

        score_text = font.render(f" Tvoje score: {final_score}", False, (0, 30, 150))
        score_text_rect = score_text.get_rect(center=(400, 75))
        player = pygame.image.load("minihry/Pokerun/Files/hrac_.png")
        player_rect = player.get_rect(midbottom=(400, 270))
        if final_score == 0:
            screen.blit(instruction, instruction_rect)
            screen.blit(player, player_rect)
        else:
            screen.blit(score_text,score_text_rect)
            screen.blit(instruction2, instruction2_rect)
            screen.blit(player, player_rect)

    pygame.display.update()
    clock.tick(60)
