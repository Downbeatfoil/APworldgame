import pygame
from sys import exit
import random


# Initialize Pygame
pygame.init()
pygame.display.set_caption('APWorldGame')
clock = pygame.time.Clock()




# Set up the game window
screen = pygame.display.set_mode((500, 600))

ocean_surface = pygame.image.load('graphics/oceanpixel-transformed.jpeg').convert()
ocean_surface = pygame.transform.scale(ocean_surface, (500, 600))

enemy_surface = pygame.image.load('graphics/piratereal.png').convert_alpha()
enemy_surface = pygame.transform.scale(enemy_surface, (100, 58))
enemy_rect = enemy_surface.get_rect(midtop = (250, 42))
enemy_surface = pygame.transform.flip(enemy_surface, True, False)


cannonball_surface = pygame.image.load('graphics/cannonball.png').convert_alpha()
cannonball_surface = pygame.transform.scale(cannonball_surface, (25, 25))

player_surface = pygame.image.load('graphics/historyship.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (68, 85))
player_rect = player_surface.get_rect(midbottom=(250, 550))  
shoot_sound = pygame.mixer.Sound('audio\cannon-fire-161072-[AudioTrimmer.com].mp3')
shoot_sound.set_volume(.08)

bg_music = pygame.mixer.Sound('audio/battle-ship-111902.mp3')
bg_music.play(loops = -1)
bg_music.set_volume(.6)


game_active = True


cannonballs = []
playercannonballs = []
count = 0

enemyspeed = -8
enemyspeedp = 8
enemy_direction = 8
hardness = 10
player_speed = 15
cannonball_speed = 8





move_left = False
move_right = False
player_can_shoot = True
cannonball_cooldown = 5  # Cooldown for player's cannonball shots
cooldown_timer = 0  # Initialize the cooldown timer to 0

# Game loop
while True:
    screen.blit(ocean_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player_can_shoot:
                playercannonball_rect = cannonball_surface.get_rect(midbottom=(player_rect.midtop[0], player_rect.midtop[1] - 5))
                shoot_sound.play()
                playercannonballs.append(playercannonball_rect)
                player_can_shoot = False
            if len(playercannonballs) == 0:
                player_can_shoot = True



        else: 
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_5):
                game_active = True
    
    if game_active:
        lose = False
        # Update player's position based on the movement flags
        if move_left:
            player_rect.x -= player_speed
        if move_right:
            player_rect.x += player_speed

        # Keep the player within the screen boundaries
        player_rect.x = max(0, min(player_rect.x, 500 - player_rect.width))

        enemy_rect.x += enemy_direction

        # Check if the enemy is out of bounds and change its direction
        if enemy_rect.right > 500:
            enemy_surface = pygame.transform.flip(enemy_surface, True, False)
            enemy_direction = enemyspeed
        elif enemy_rect.left < 0:
            enemy_surface = pygame.transform.flip(enemy_surface, True, False)
            enemy_direction = enemyspeedp

        screen.blit(enemy_surface, enemy_rect)
        screen.blit(player_surface, player_rect)

        screen.blit(enemy_surface, enemy_rect)
        screen.blit(player_surface, player_rect)

        for playercannonball_rect in playercannonballs:
            playercannonball_rect.y -= cannonball_speed  # Change to -= to move upwards
            if playercannonball_rect.bottom < 0:
                playercannonballs.pop(0)  # Remove when it goes above the screen

            if playercannonball_rect.colliderect(enemy_rect):
                playercannonballs.remove(playercannonball_rect)
                move_left = False
                move_right = False
                game_active = False
                kabir = 0
            
            screen.blit(cannonball_surface, playercannonball_rect)

        if random.randint(1, 100) < hardness:
            cannonball_rect = cannonball_surface.get_rect(midtop=(enemy_rect.midbottom[0], enemy_rect.midbottom[1] + 5))
            cannonballs.append(cannonball_rect)
            shoot_sound.play()
            count += 1
        # Update and draw cannonballs
        for cannonball_rect in cannonballs:
            cannonball_rect.y += cannonball_speed

            if len(playercannonballs) == 1 and playercannonball_rect.colliderect(cannonball_rect):
                playercannonballs.remove(playercannonball_rect)
                cannonballs.remove(cannonball_rect)

            if cannonball_rect.colliderect(player_rect):
                cannonballs.remove(cannonball_rect)
                move_left = False
                move_right = False
                lose = True
                game_active = False

            # Remove cannonball when it leaves the screen
            if cannonball_rect.top > 600:
                cannonballs.remove(cannonball_rect)

            screen.blit(cannonball_surface, cannonball_rect)
            
        


    else:
        if lose: 
            screen.fill('Red')
            cannonballs = []
            playercannonballs = []
            count = 0
        else: 
            screen.fill('Green')
            kabir += 1
            if kabir < 2:
                print(count)
            cannonballs = []
            playercannonballs = []



    pygame.display.update()


    
    clock.tick(60)


