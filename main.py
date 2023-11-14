import pygame
from sys import exit
import random
from statistics import mean 
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
        global score_percent
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

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 350, 300))

    money_text = test_font.render(f"Doubloons: {player_money}", True, (255, 255, 255))
    sails_text = test_font.render(f"Sails: {num_sails}", True, (255, 255, 255))
    astrolabe_text = test_font.render(f"Astrolabe: {'Yes' if has_astrolabe else 'No'}", True, (255, 255, 255))
    compass_text = test_font.render(f"Compass: {'Yes' if has_compass else 'No'}", True, (255, 255, 255))
    map_text = test_font.render(f"Map: {'Yes' if has_map else 'No'}", True, (255, 255, 255))
    cbspeed_text = test_font.render(f"Gunpowder Quality: {player_cannonball_speed}", True, (255, 255, 255))
    hull_text = test_font.render(f"Hull Thickness: {hull_thickness}", True, (255, 255, 255))
    global current_level, level_scores
    current_level = 1
    level_scores = []

    screen.blit(money_text, (10, 10))
    screen.blit(sails_text, (10, 50))
    screen.blit(astrolabe_text, (10, 90))
    screen.blit(compass_text, (10, 130))
    screen.blit(map_text, (10, 170))
    screen.blit(cbspeed_text,(10, 210))
    screen.blit(hull_text,(10, 250))

    pygame.display.flip()

def display_level_complete_screen(astrolabe, compass, map):
    screen.fill('Blue')  # You can use a different color or background image
    if check_get_lost(astrolabe, compass, map):
        display_lost_message(astrolabe, compass, map)
    else: 
        if current_level != 5:
            level_complete_text = test_font.render(f"Get Ready For Level {current_level}", True, (255, 255, 255))
            level_complete_rect = level_complete_text.get_rect(center=(250, 100))
            screen.blit(level_complete_text, level_complete_rect)
        if current_level ==2:
            pirate_text = test_font.render(
            "You will fight Captain Kidd",
            True,
            (255, 255, 255)
            )

            pirate_rect = pirate_text.get_rect(center=(250, 250))
            screen.blit(pirate_text, pirate_rect)

            # Load and display the pirate image
            pirate_image = pygame.image.load('graphics\captain-william-kidd-privateer-and-pirate-shanina-conway.jpg').convert_alpha()
            pirate_image = pygame.transform.scale(pirate_image, (180, 250))
            pirate_rect = pirate_image.get_rect(center=(250, 420))
            screen.blit(pirate_image, pirate_rect)

            pygame.display.flip()

            # Add a delay to show the start screen for a moment
            pygame.time.delay(5000)  # Adjust the delay time as needed
            global starttime
            starttime = pygame.time.get_ticks() 
            # Reset necessary variables for the next level
            reset_game_state()
        if current_level ==3:
            pirate_text = test_font.render(
            "You will fight Blackbeard",
            True,
            (255, 255, 255)
            )

            pirate_rect = pirate_text.get_rect(center=(250, 250))
            screen.blit(pirate_text, pirate_rect)

            # Load and display the pirate image
            pirate_image = pygame.image.load('graphics/blackbeard.jpg').convert_alpha()
            pirate_image = pygame.transform.scale(pirate_image, (150, 250))
            pirate_rect = pirate_image.get_rect(center=(250, 420))
            screen.blit(pirate_image, pirate_rect)

            pygame.display.flip()

            # Add a delay to show the start screen for a moment
            pygame.time.delay(5000)  # Adjust the delay time as needed

            starttime = pygame.time.get_ticks() 
            # Reset necessary variables for the next level
            reset_game_state()
        if current_level ==4:
            pirate_text = test_font.render(
            "You will fight Shiv Garg",
            True,
            (255, 255, 255)
            )

            pirate_rect = pirate_text.get_rect(center=(250, 250))
            screen.blit(pirate_text, pirate_rect)

            # Load and display the pirate image
            pirate_image = pygame.image.load('graphics\IMG_6893.jpg').convert_alpha()
            pirate_image = pygame.transform.scale(pirate_image, (150, 250))
            pirate_rect = pirate_image.get_rect(center=(250, 420))
            screen.blit(pirate_image, pirate_rect)

            pygame.display.flip()

            # Add a delay to show the start screen for a moment
            pygame.time.delay(5000)  # Adjust the delay time as needed
            starttime = pygame.time.get_ticks() 
            # Reset necessary variables for the next level
            reset_game_state()
        if current_level == 5:
            pirate_text = test_font.render(
            "You Won!",
            True,
            (255, 255, 255)
            )
            pirate_rect = pirate_text.get_rect(center=(250, 250))
            screen.blit(pirate_text, pirate_rect)
            global level_scores
            avgscore = mean(level_scores)
            avg_text = test_font.render(f"Average Score: {avgscore}", True, (255, 255, 255))
            avg_rect = avg_text.get_rect(center=(250, 300))
            screen.blit(avg_text, avg_rect)

            pygame.display.flip()
            pygame.time.delay(8000)
            pygame.quit()
            exit()

def displaystart():
    screen.fill((0, 0, 255))  # Change the background color to blue
    start_text = test_font.render("Get ready for level 1", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(250, 100))
    screen.blit(start_text, start_rect)

    # Display additional text
    pirate_text = test_font.render(
    "You will fight Calico Jack",
    True,
    (255, 255, 255)
    )

    pirate_rect = pirate_text.get_rect(center=(250, 250))
    screen.blit(pirate_text, pirate_rect)

    # Load and display the pirate image
    pirate_image = pygame.image.load('graphics\john-calico-jack-rackham-1680-1720-print-collector.jpg').convert_alpha()
    pirate_image = pygame.transform.scale(pirate_image, (150, 250))
    pirate_rect = pirate_image.get_rect(center=(250, 420))
    screen.blit(pirate_image, pirate_rect)

    pygame.display.flip()

    # Add a delay to show the start screen for a moment
    pygame.time.delay(5000)  # Adjust the delay time as needed
    

def reset_game_state():
    global game_active, hit, cannonballs, playercannonballs
    cannonballs = []
    playercannonballs = []
    game_active = True

def calculate_get_lost_chance(astrolabe, compass, map):
    total_tools = astrolabe + compass + map
    if total_tools == 0:
        return 60
    elif total_tools == 1:
        return 35
    elif total_tools == 2:
        return 20
    else:
        return 0

def check_get_lost(astrolabe, compass, map):
    chance = calculate_get_lost_chance(astrolabe, compass, map)
    if random.randint(1, 100) <= chance:
        return True
    return False

def display_lost_message(astrolabe, compass, map):
    if astrolabe == 0 and map == 0 and compass == 0:
        message = "No Navigation Tools? Rethink your finances..."
    elif astrolabe == 0 and map == 0:
        message = "Did you really think you could have gotten home without an astrolabe and map?"
    elif astrolabe == 0 and compass == 0:
        message = "Lost without an astrolabe and compass? Better luck next time!" 
    elif compass == 0 and map == 0:
        message = "Navigating without a compass and map? That's a tough journey!"
    else:
        message = "Lost at sea! Better luck next time."
    
    real = 'You Got Lost!'
    text_surface = test_font.render(real, True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(center=(250, 300))
    screen.fill('blue')
    screen.blit(text_surface, text_rect)
    print(message)
    global enemyspeed, enemyspeedp, hardness, num_sails, player_speed, player_cannonball_speed, has_astrolabe, has_compass, has_map, hull_thickness, player_money
    enemyspeed = -8
    enemyspeedp = 8
    hardness = 5
    num_sails = 1
    player_speed = 5
    player_cannonball_speed = 5
    has_astrolabe = False
    has_compass = False
    has_map = False
    hull_thickness = 0
    player_money = 100
    pygame.display.flip()  # Update the display
    pygame.time.delay(5000)
    global cannonballs, playercannonballs
    cannonballs = []
    playercannonballs = []
     
    display_restart_screen()

# Initialize Pygame
pygame.init()
pygame.display.set_caption('APWorldGame')
clock = pygame.time.Clock()
global starttime
starttime = 0
global current_level
current_level = 1

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
global level_scores
level_scores = []  
global cannonballs
cannonballs = []
global playercannonballs
playercannonballs = []

global num_sails
num_sails = 1
global player_money
player_money = 100
global enemyspeed
enemyspeed = -8
global enemyspeedp
enemyspeedp = 8
enemy_direction = 8
global hardness
hardness = 5
global player_speed
player_speed = 5
cannonball_speed = 8
global player_cannonball_speed
player_cannonball_speed = 5
global has_astrolabe
has_astrolabe = False
global has_compass
has_compass = False
global has_map
has_map = False
global hull_thickness
hull_thickness = 0
hit = 0

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
                        player_speed += 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                   if player_money >= 10:
                        if not has_astrolabe:
                            has_astrolabe = True
                            player_money -= 10
                   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                   if player_money >= 10:
                        if not has_compass:
                            has_compass = True
                            player_money -= 10

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                   if player_money >= 10:
                        if not has_map:
                            has_map = True
                            player_money -= 10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5:
                   if player_money >= 15:
                        player_cannonball_speed += 2
                        player_money -= 15
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_6:
                   if player_money >= 20:
                        hull_thickness += 1
                        player_money -= 20

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                displaystart()
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
            playercannonball_rect.y -= player_cannonball_speed  # Change to -= to move upwards
            if playercannonball_rect.bottom < 0:
                playercannonballs.pop(0)  # Remove when it goes above the screen

            if playercannonball_rect.colliderect(enemy_rect):
                playercannonballs.remove(playercannonball_rect)
                move_left = False
                move_right = False
                game_active = False
                if score_percent > 100:
                    score_percent = 100
                level_scores.append(score_percent)
                # Transition to the next level
                current_level += 1
                hardness += 2  # Increase hardness for the next level
                enemyspeed -= 4  # Increase enemy speed for the next level
                enemyspeedp += 4
                print(level_scores)
                display_level_complete_screen(has_astrolabe, has_compass, has_map)

            screen.blit(cannonball_surface, playercannonball_rect)

        if random.randint(1, 100) < hardness:
            cannonball_rect = cannonball_surface.get_rect(midtop=(enemy_rect.midbottom[0], enemy_rect.midbottom[1] + 5))
            cannonballs.append(cannonball_rect)
            shoot_sound.play()
        # Update and draw cannonballs
        for cannonball_rect in cannonballs:
            cannonball_rect.y += cannonball_speed

            if len(playercannonballs) == 1 and playercannonball_rect.colliderect(cannonball_rect):
                playercannonballs.remove(playercannonball_rect)
                cannonballs.remove(cannonball_rect)

            if cannonball_rect.colliderect(player_rect):
                cannonballs.remove(cannonball_rect)
                hit += 1
                if hit > hull_thickness:
                    print('yo')
                    move_left = False
                    move_right = False
                    enemyspeed = -8
                    enemyspeedp = 8
                    hardness = 5
                    num_sails = 1
                    player_speed = 5
                    player_cannonball_speed = 5
                    has_astrolabe = False
                    has_compass = False
                    has_map = False
                    hull_thickness = 0
                    player_money = 100
                    hit = 0
                    game_active = False

            


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


