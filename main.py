import pygame
from sys import exit
import random
duration = 105000

def get_color(score):
    if score >= 90:
        return (0, 255, 0)  # Green
    elif 70 <= score < 90:
        return (255, 165, 0)  # Orange/Yellow
    else:
        return (255, 0, 0)  # Red

def displayscore():
        pygame.draw.rect(screen, (0, 0, 0), (200, 0, 100, 30))
        currenttime = duration - ((pygame.time.get_ticks()) -starttime)
        score_percent = (currenttime / 100000 * 100)
        score_percent = round(score_percent)
        
        if (pygame.time.get_ticks() - starttime) > 5000:
            score_surf = test_font.render(f'{score_percent}%', True, get_color(score_percent))
            score_rect = score_surf.get_rect(center=(250, 20))
            screen.blit(score_surf, score_rect)
        else:
            score_surf = test_font.render('100%', True, get_color(100))
            score_rect = score_surf.get_rect(center=(250, 20))
            screen.blit(score_surf, score_rect)

def display_restart_screen():
    screen.fill('Red')
    pygame.draw.rect(screen, (0, 0, 0), (85, 370, 330, 50))
    screen.blit(start_text, start_rect)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 250, 260))

    money_text = test_font.render(f"Money: {player_money}", True, (255, 255, 255))
    sails_text = test_font.render(f"Sails: {num_sails}", True, (255, 255, 255))
    speed_text = test_font.render(f"Speed: {player_speed}", True, (255, 255, 255))
    astrolabe_text = test_font.render(f"Astrolabe: {'Yes' if has_astrolabe else 'No'}", True, (255, 255, 255))
    compass_text = test_font.render(f"Compass: {'Yes' if has_compass else 'No'}", True, (255, 255, 255))
    map_text = test_font.render(f"Map: {'Yes' if has_map else 'No'}", True, (255, 255, 255))



    screen.blit(money_text, (10, 10))
    screen.blit(sails_text, (10, 50))
    screen.blit(speed_text, (10, 90))
    screen.blit(astrolabe_text, (10, 130))
    screen.blit(compass_text, (10, 170))
    screen.blit(map_text, (10, 210))

    pygame.display.flip()


# Initialize Pygame
pygame.init()
pygame.display.set_caption('APWorldGame')
clock = pygame.time.Clock()
starttime = 0



# Set up the game window
screen = pygame.display.set_mode((500, 600))

test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)

start_text = test_font.render("Press 'S' to start", True, (255, 255, 255))
start_rect = start_text.get_rect(center=(250, 400))

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


game_active = False


cannonballs = []
playercannonballs = []
count = 0

num_sails = 1
player_money = 100
enemyspeed = -8
enemyspeedp = 8
enemy_direction = 8
hardness = 5
player_speed = 5
cannonball_speed = 8
has_astrolabe = False
has_compass = False
has_map = False


show_start_screen = True


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
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # User pressed the "1" key
                    if player_money >= 10:  # Assuming the cost to subtract is 10 money units
                        player_money -= 10
                        num_sails += 1
                        player_speed += 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                   has_astrolabe = True
                   player_money -= 10
                   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                   has_compass = True
                   player_money -= 10

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                   has_map = True
                   player_money -= 10

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                game_active = True
                starttime = pygame.time.get_ticks() 
    
    if game_active:
        displayscore()
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


        for playercannonball_rect in playercannonballs:
            playercannonball_rect.y -= cannonball_speed  # Change to -= to move upwards
            if playercannonball_rect.bottom < 0:
                playercannonballs.pop(0)  # Remove when it goes above the screen

            if playercannonball_rect.colliderect(enemy_rect):
                playercannonballs.remove(playercannonball_rect)
                move_left = False
                move_right = False
                game_active = False
            
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
                game_active = False
                kabir = 0


            # Remove cannonball when it leaves the screen
            if cannonball_rect.top > 600:
                cannonballs.remove(cannonball_rect)

            screen.blit(cannonball_surface, cannonball_rect)
            
        


    else:
        display_restart_screen()
        cannonballs = []
        playercannonballs = []
            


    pygame.display.update()


    
    clock.tick(30)


