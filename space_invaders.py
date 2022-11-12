### Module, Functins & Setting imports ####################################################################################################
import pygame   # imports the pygame modules to enable their use within the program
import os       # define file paths to image and sound files that should work across differing operating systems - windows, Apple etc.
import random   # imports random module to allow randomly select an enemy ship to automatically fire

from pygame.event import wait  # required for wait msec delay command - wait (1000)
from os.path import exists     # required for checking high score file exists function - exists()
from game_setting import *     # imports all constant variable settings from file - game_setting.py 

pygame.font.init()  # initiate font module to handle game screen text
pygame.mixer.init() # initiate sound module to handle game sound effects
###########################################################################################################################################

### Define USER events ####################################################################################################################
PLAYER_HIT = pygame.USEREVENT + 1     # posts a user specified event when player hit to action specific code
ENEMY_HIT = pygame.USEREVENT + 2      # posts a user specified when player hit to action specific code
PLAYER_KILLED = pygame.USEREVENT + 3  # posts a user specified when player hit to action specific code
###########################################################################################################################################

### load external image  files - define paths #############################################################################################
game_window_icon = pygame.image.load(os.path.join("Images and sounds","darth vader.png"))             # game window icon image file
backdrop_image = pygame.image.load(os.path.join("Images and sounds","backdrop 1.png"))                # play window backdrop image file
game_over_image = pygame.image.load(os.path.join("Images and sounds","game_over.png"))                # game over backdrop image file
start_screen_image = pygame.image.load(os.path.join("Images and sounds","start_screen.png"))          # start screen backdrop image file
player_spaceship_image = pygame.image.load(os.path.join("Images and sounds","x wing.png"))            # player spaceship image file
enemy_spaceship_image = pygame.image.load(os.path.join("Images and sounds","enemy.png"))              # enemy spaceship image file
enemy_spaceship_1_image = pygame.image.load(os.path.join("Images and sounds","enemy1.png"))           # enemy 2nd spaceship image file
spaceship_destroyed_image = pygame.image.load(os.path.join("Images and sounds","ship_destroyed.png")) # loading spaceship explosion image file
###########################################################################################################################################

### Scale Image files #####################################################################################################################
backdrop = pygame.transform.scale(backdrop_image, (WINDOW_WIDTH, WINDOW_HEIGHT))                      # scale backdrop to fit game window
game_over_backdrop = pygame.transform.scale(game_over_image, (WINDOW_WIDTH, WINDOW_HEIGHT))           # scale game over backdrop to fit game window
start_screen_backdrop = pygame.transform.scale(start_screen_image, (WINDOW_WIDTH, WINDOW_HEIGHT))     # scale start screen backdrop to fit game window
player_lives_image = pygame.transform.scale(player_spaceship_image, (SCALE_WIDTH//2, SCALE_HEIGHT//2))# small spaceships for remaining lives indication
player_spaceship = pygame.transform.scale(player_spaceship_image, (SCALE_WIDTH, SCALE_HEIGHT))        # player spaceship to scale varibale, so can resize if needed
enemy_spaceship = pygame.transform.scale(enemy_spaceship_image, (SCALE_WIDTH, SCALE_HEIGHT))          # enemy spaceship to scale varibale, so can resize if needed
enemy_spaceship_1 = pygame.transform.scale(enemy_spaceship_1_image, (SCALE_WIDTH, SCALE_HEIGHT))      # enemy 2nd spaceship to scale varibale, so can resize if needed
spaceship_destroyed = pygame.transform.scale(spaceship_destroyed_image, (SCALE_WIDTH, SCALE_HEIGHT))  # spaceship explosion to scale varibale, so can resize if needed
###########################################################################################################################################

### load external sound files - define paths ##############################################################################################
player_shot_sound = pygame.mixer.Sound(os.path.join("Images and sounds","shoot.wav"))        # player fire sound file load
explosion_sound = pygame.mixer.Sound(os.path.join("Images and sounds","explosion.wav"))      # player hit explosion sound file load
enemy_kill_sound = pygame.mixer.Sound(os.path.join("Images and sounds","invaderkilled.wav")) # enemy hit/kill explosion sound file load
###########################################################################################################################################

### Set Volume ##############################################################################################
player_shot_sound.set_volume(0.0)
explosion_sound.set_volume(0.0)
enemy_kill_sound.set_volume(0.0)
###########################################################################################################################################

### Set up Game Window ####################################################################################################################
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # setting the game window size using the width, height variables
pygame.display.set_caption(GAME_TITLE)                        # setting the game window caption to the game title
pygame.display.set_icon(game_window_icon)                     # setting the game window icon to the image file loaded
###########################################################################################################################################

##### START GAME LOOP & SPLASH SCREEN #####################################################################################################
def start_screen():                             # define start screen function - no variables passed to it
    run = True                                  # assign loop variable to True
    while run:                                  # loop while "run" is True
        WIN.blit(start_screen_backdrop, (0, 0)) # set start screen background surface image
        pygame.display.update()                 # send surface to display in game window
        for event in pygame.event.get():        # use pygame event get function to wait for user to either "press key to start" or Quit
            if event.type == pygame.QUIT:       # user has selected to Quit game
                pygame.quit()                   # call pygame quit function to close window and stop program
            if event.type == pygame.KEYDOWN:    # pygame has detected key pressed event, user wants to start game 
                main()                          # call main game function to start the game
###########################################################################################################################################

##### GAME OVER LOOP & SPLASH SCREEN ######################################################################################################
def game_over_screen(player_score, high_score):                           # define game over screen function, and variables passed to it
    display_font = pygame.font.SysFont("msgothicmsuigothicmspgothic", 40) # use pygame module to set font for text

    if player_score < high_score:                                                             # if player did not get new high score        
        line_1 = display_font.render ("HIGH SCORE: " + str(high_score), 1, (255, 255, 255))   # line_1 display existing high score
        line_2 = display_font.render ("YOU SCORED: " + str(player_score), 1, (255, 255, 255)) # line_2 display player score

    elif player_score == high_score:                                                                         # else if player equals high score
        line_1 = display_font.render ("YOU EQUALLED THE HIGH SCORE: " + str(high_score), 1, (255, 255, 255)) # line_1 displays text high score equalled
        line_2 = display_font.render ("YOU SCORED: " + str(player_score), 1, (255, 255, 255))                # line_2 display player score

    elif player_score > high_score:                                         # else if player gets new high score
        high_score = player_score                                           # set new high score value
        with open(os.path.join(HIGH_SCORE_FILE), 'w') as high_score_file :  # open high score file
            high_score_file.write(str(high_score))                          # write new high score to file
        line_1 = display_font.render ("NEW HIGH SCORE ! " + str(high_score), 1, (255, 255, 255)) # line_1 displays new high score
        line_2 = display_font.render ("THE FORCE IS STRONG IN YOU", 1, (255, 255, 255))          # line_2 displays message text

    run = True                                  # assign loop variable to True
    while run:                                  # loop while "run" is True
        WIN.blit(game_over_backdrop, (0, 0))    # set game over screen background surface image
        pygame.draw.rect(game_over_backdrop, YELLOW, pygame.Rect(TEXTBOX_X - 5, TEXTBOX_Y -5, TEXTBOX_WIDTH + 10, TEXTBOX_HEIGHT + 10)) # draw textbox background
        pygame.draw.rect(game_over_backdrop, GREY, pygame.Rect(TEXTBOX_X, TEXTBOX_Y, TEXTBOX_WIDTH, TEXTBOX_HEIGHT))                    # draw textbox rect
        WIN.blit(line_1, (TEXTBOX_X + TEXTBOX_WIDTH/2 - line_1.get_width()/2, TEXTBOX_Y + 20))  # draw line 1 text on top of textbox rectangle
        WIN.blit(line_2, (TEXTBOX_X + TEXTBOX_WIDTH/2 - line_2.get_width()/2, TEXTBOX_Y + 60))  # draw line 2 text on top of textbox rectangle
        pygame.display.update()                                                                 # update display with draw command info
        
        for event in pygame.event.get():        # use pygame event get function to wait for user to either "press key to restart" or Quit
            if event.type == pygame.QUIT:       # user has selected to Quit game
                pygame.quit()                   # call pygame quit function to close window and stop program
            if event.type == pygame.KEYDOWN:    # pygame has detected key pressed event, user wants to restart game 
                main()                          # call main game function to restart the game
###########################################################################################################################################

### Player Spaceship movement function ####################################################################################################
def player_movement (key_pressed, player_position):                            # define player spaceship movement function, and variables passed to it
    if key_pressed[pygame.K_LEFT] and player_position.x - PLAYER_VELOCITY > 0: # if player wants move left "AND" move left will keep spaceship on the screen
        player_position.x -= PLAYER_VELOCITY                                   # move player spaceship left at set velocity number of pixels 
    if key_pressed[pygame.K_RIGHT]and player_position.x + player_position.width + PLAYER_VELOCITY < WINDOW_WIDTH: # move player right but keep on screen
        player_position.x += PLAYER_VELOCITY                                   # move player spaceship right at set velocity number of pixels 
###########################################################################################################################################

### Enemy Spawn function ##################################################################################################################
def enemy_spawn (enemy_list):   # define enemy spawn function, and variables passed to it
    x_position = 150            # set initial enemy rectangle x value
    y_position = 50             # set initial enemy rectangle y value
    i = 0                       # set loop iteration count to 0

    enemy_position = pygame.Rect(x_position, y_position, SCALE_WIDTH, SCALE_HEIGHT) # define rectangle to represent enemy position to control of movement

    while i < 10:               # loop while i is less than 10
        enemy_position = pygame.Rect(x_position, y_position, SCALE_WIDTH, SCALE_HEIGHT) # create new enemy position
        x_position += 100       # each loop increase x value by 100
        enemy = enemy_position  # give position to the enemy
        enemy_list.append(enemy)# add the newenemy to the enemy list
        i += 1                  # increment loop counter
###########################################################################################################################################

### Enemy Spaceships movement down the screen #############################################################################################
def enemy_movement (enemy_list, enemy_missile, level):                      # define enemy movement function, and variables passed to it
    speed = ENEMY_VELOCITY + level                                          # enemy speed increases each level

    for enemy in enemy_list:                                                # for each enemy in the enemy list
        if enemy.x + SCALE_WIDTH < WINDOW_WIDTH - 25 and enemy.y == 50:     # if moving left would keep enemy on screen
            enemy.x += speed                                                # then move left at current level speed
        elif enemy.x > 25 and enemy.y == 125:                               # if moving right would keep enemy on screen
            enemy.x -= speed                                                # then move right at current level speed
        elif enemy.x + SCALE_WIDTH < WINDOW_WIDTH - 25 and enemy.y == 200:  # if moving left would keep enemy on screen
            enemy.x += speed                                                # then move left at current level speed
        elif enemy.x > 25 and enemy.y == 275:                               # if moving right would keep enemy on screen
            enemy.x -= speed                                                # then move right at current level speed
        elif enemy.x + SCALE_WIDTH < WINDOW_WIDTH - 25 and enemy.y == 350:  # if moving left would keep enemy on screen
            enemy.x += speed                                                # then move left at current level speed
        elif enemy.x > 25 and enemy.y == 425:                               # if moving right would keep enemy on screen
            enemy.x -= speed                                                # then move right at current level speed
        elif enemy.x + SCALE_WIDTH < WINDOW_WIDTH - 25 and enemy.y == 500:  # if moving left would keep enemy on screen
            enemy.x += speed                                                # then move left at current level speed
        elif enemy.x > 25 and enemy.y == 575:                               # if moving right would keep enemy on screen
            enemy.x -= speed                                                # then move right at current level speed                     
        elif enemy.x + SCALE_WIDTH < WINDOW_WIDTH - 25 and enemy.y == 650:  # if moving left would keep enemy on screen
            enemy.x += speed                                                # then move left at current level speed
        elif enemy.x > 25 and enemy.y == 725:                               # if moving right would keep enemy on screen
            enemy.x -= speed                                                # then move right at current level speed
        elif enemy.x + SCALE_WIDTH < WINDOW_WIDTH - 25 and enemy.y == 700:  # if moving left would keep enemy on screen
            enemy.x += ENEMY_VELOCITY + level                               # then move left at current level speed
        elif enemy.x + SCALE_WIDTH >= WINDOW_WIDTH - 25 or enemy.x + SCALE_WIDTH <= WINDOW_WIDTH + 25: # if enemy is near edge of screen
            enemy.y += 75                                                                              # move enemy down
###########################################################################################################################################

### random enemy missile firing ###########################################################################################################
def enemy_missile_handling (enemy_list, enemy_missile, level):                    # define enemy missile firing function, and variables passed to it

    if len(enemy_list) > 0 and len(enemy_missile) < (MAX_ENEMY_MISSILES + level): # if enemies exist and max number of missiles dont already exist on screen
        select_ramdon_enemy = (random.randint(0,len(enemy_list)-1))               # pick random number between 0 -> number of current enemys in list
        random_enemy = enemy_list[select_ramdon_enemy]                            # get position of random enemy from enemy list
        missile = pygame.Rect(random_enemy.x + SCALE_WIDTH//2, random_enemy.y + SCALE_HEIGHT//2, 2, 10) # missile fired from position of random enemy
        enemy_missile.append(missile)                                             # missile loaded into list for tracking
        player_shot_sound.play()                                                  # play missile fired sound
###########################################################################################################################################

### Missile/Collision handling function ###################################################################################################
def collision_handling (player_missile, enemy_missile, player_position, enemy_list): # define collision handling function, and variables passed to it

    ### Player Missile Collision tracking ###
    for missile in player_missile:                                   # for each missile in the player missiles list
        missile.y -= MISSILE_VELOCITY                                # move each missile up the screen, at set velocity number of pixels
        if missile.y < 0:                                            # check if missile is still on the screen
            player_missile.remove(missile)                           # remove missile from list once it goes off the bottom of the screen
        for enemy in enemy_list:                                     # for each enemy in the enemy list
            if enemy.colliderect(missile):                           # if missile collision with enemy spaceship is detected
                player_missile.remove(missile)                       # remove the specific missile from the player missile list
                enemy_kill_sound.play()                              # play sound for enemy hit/kill
                enemy_list.remove(enemy)                             # remove the killed enemy from enemy list
                pygame.event.post(pygame.event.Event(ENEMY_HIT))     # post enemy hit use defined event to increment player score
                    
    ### Enemy Missile Collision tacking ###
    for missile in enemy_missile:                                    # for each missile in the enemy missiles list
        missile.y += MISSILE_VELOCITY                                # move each missile down the screen, at set velocity number of pixels
        if player_position.colliderect(missile):                     # if collision with player spaceship is detected
            enemy_missile.remove(missile)                            # remove the specific missile from the list
            explosion_sound.play()                                   # play explosion sound for player hit
            pygame.event.post(pygame.event.Event(PLAYER_HIT))        # trigger event to deal with missile hit, reduce player health by set amount
        elif missile.y > WINDOW_HEIGHT:                              # else if missile missed the player, check if missile is still on the screen
            enemy_missile.remove(missile)                            # remove missile from list once it goes off the bottom of the screen

    ### Enemy & Player Collision event ###
    for enemy in enemy_list:                                         # for each enemy in the enemy list
        if player_position.colliderect(enemy):                       # if collision with player spaceship is detected
            explosion_sound.play()                                   # play explosion sound for player hit
            enemy_list.clear()                                       # clear enemy list as they have reached bottom of screen where player ship is
            pygame.event.post(pygame.event.Event(PLAYER_KILLED))     # trigger event to deal with player hit, lose life
###########################################################################################################################################

### Display update function ###############################################################################################################
def display_update (player_position, player_missile, enemy_missile, enemy_list, player_score, player_health, player_lives, high_score, level): # define display function and parameters passed

    display_font = pygame.font.SysFont("msgothicmsuigothicmspgothic", 30)  # use pygame module to set font for text
    
    ### Game text display setup ###
    WIN.blit(backdrop, (0, 0))                                                                                              # load space backdrop to fill game display background
    WIN.blit((display_font.render (("High-Score: " + str(high_score)), 1, (WHITE))), (10, GAME_TEXT_Y_POS))                 # high score display info
    WIN.blit((display_font.render (("Score: " + str(player_score)), 1, (WHITE))), (350, GAME_TEXT_Y_POS))                   # player score display info
    WIN.blit((display_font.render (("Level: " + str(level)), 1, (WHITE))), (600, GAME_TEXT_Y_POS))                          # game level display info
    WIN.blit((display_font.render (("Health: "), 1, (WHITE))), ((HEALTH_BAR_X_POS - 75), GAME_TEXT_Y_POS))                  # health text display info
    WIN.blit(display_font.render (("Lives: " +str(player_lives)), 1, (WHITE)), ((HEALTH_BAR_X_POS + 310), GAME_TEXT_Y_POS)) # lives text display info
    
    ### Health bar display handling ###
    health_bar_red = (pygame.Rect(HEALTH_BAR_X_POS, GAME_TEXT_Y_POS, 100, (GAME_TEXT_Y_POS+2)))                 # setup position & size of background health bar
    pygame.draw.rect(WIN, RED, health_bar_red)                                                                  # draw RED health bar, behind green or amber bar
    if player_health > 40:                                                                                      # if player health is above 40% - healthy
        health_bar_green = (pygame.Rect(HEALTH_BAR_X_POS, GAME_TEXT_Y_POS, player_health, (GAME_TEXT_Y_POS+2))) # setup position & size of health bar
        pygame.draw.rect(WIN, GREEN, health_bar_green)                                                          # draw GREEN health bar, on top of background health bar
    elif player_health <= 40:                                                                                   # if player health is below 40% - low warning
        health_bar_amber = (pygame.Rect(HEALTH_BAR_X_POS, GAME_TEXT_Y_POS, player_health, (GAME_TEXT_Y_POS+2))) # setup position & size of health bar
        pygame.draw.rect(WIN, AMBER, health_bar_amber)                                                          # draw AMBER health bar, on top of background health bar

    ### Display Lives remaining spaceship icons ###
    if player_lives == 3:                                             # if player has 3 lives
        WIN.blit(player_lives_image,((HEALTH_BAR_X_POS + 450), 5))    # display remaining life small ship 1
        WIN.blit(player_lives_image,((HEALTH_BAR_X_POS + 400), 5))    # display remaining life small ship 2
    elif player_lives == 2:                                           # if player has 2 lives
        WIN.blit(player_lives_image,((HEALTH_BAR_X_POS + 400), 5))    # display remaining life small ship 1
    elif player_lives == 0:                                           # if player has 0 lives
        game_over_screen(player_score, high_score)                    # call game over function, passing player score and high score

    ### Display game items player, enemy and missiles ###
    WIN.blit(player_spaceship,(player_position.x, player_position.y)) # draw player at x, y position of the rectangle passed from main()

    for enemy in enemy_list:                    # for each enemy in the enemy list
        if (level % 2) == 0:                    # if game level is even
            WIN.blit(enemy_spaceship,(enemy))   # draw enemy spaceship
        else:                                   # else game level must be odd so want to display different spaceship
            WIN.blit(enemy_spaceship_1,(enemy)) # draw alternate enemy spaceship image
    
    for missile in player_missile:              # for every missile in player missile list
        pygame.draw.rect(WIN, GREEN, missile)   # draw missiles GREEN

    for missile in enemy_missile:               # for every missile in enemy missile list
        pygame.draw.rect(WIN, RED, missile)     # draw missile RED

    pygame.display.update()                     # redraw/update the display
###########################################################################################################################################

### Main game loop ########################################################################################################################
def main(): #define main game loop function
    
    enemy_list = []        # enemy tracking list
    player_missile = []    # player missile tracking list
    enemy_missile = []     # enemy missile tracking list
    
    ### Define Variables ###
    player_lives = 3       # define variable and initial value
    player_health = 100    # define variable and initial value 
    player_score = 0       # define variable and initial value
    level = 1              # game difficulty level

    ### Open or Create High Score file - then read data from it ###
    file_exists = exists(HIGH_SCORE_FILE)                                 # check if high score file exists    
    if file_exists == False:                                              # if high score file does not exist
        with open(os.path.join(HIGH_SCORE_FILE), 'w') as high_score_file: # create high score text file as "high_score_file"
            high_score = 0                                                # set high_score to 0 because file did not exist, thus contains no data
    elif file_exists == True:                                             # else if the file did exist
        with open(os.path.join(HIGH_SCORE_FILE), 'r') as high_score_file: # open the file to read as "high_score_file"
            filesize = os.path.getsize(HIGH_SCORE_FILE)                   # need to check file is not empty to avoid errors
            if filesize == 0:                                             # if file quals 0, file is empty so cannot be assigned to high score variable  
                high_score = 0                                            # set high score to 0
            else:                                                         # file must contain a high score already
                high_score = int(high_score_file.read())                  # set high score to the integer value of the string held in the text file

    ### player start position ###
    player_position = pygame.Rect(WINDOW_WIDTH//2, 685, SCALE_WIDTH, SCALE_HEIGHT) # define rectangle to represent player position to control of movement

    ### Enemy Spawn first wave ###
    enemy_spawn (enemy_list)                            # call function to load wave of 10 enemy spaceships

    ### MAIN GAME LOOP ###
    game_speed_clock = pygame.time.Clock()              # control the speed of the game loop so it runs same speed on different pc's/laptop etc.
    loop = True                                         # assign loop variable to True
    while loop:                                         # Run the main game loop while "run" is True                 
        game_speed_clock.tick(DISPLAY_UPDATE_SPEED_FPS) # set speed of game loop in FPS Frames Per Seond 
        for event in pygame.event.get():                # use pygame event get function to check if user Quits
            if event.type == pygame.QUIT:               # user has selected to Quit game
                quit()                                  # call pygame quit function to close window and stop program

            ### USER Event Handling ###
            if event.type == ENEMY_HIT:                          # enemy hit user configurable event detected
                player_score += (ENEMY_KILL_VALUE + (level * 5)) # add kill value to players score
                if len(enemy_list) == 0:                         # if player has killed all enemy spaceship (completed level)
                    level += 1                                   # go to next level which increases enemy speed and max number of missiles
                    enemy_spawn (enemy_list)                     # call function to load new wave of 10 enemy spaceships
                    
            if event.type == PLAYER_KILLED:                      # player live lost user configurable event detected
                player_lives -= 1                                # player loses a live
                WIN.blit(spaceship_destroyed, (player_position)) # Set ship destroyed image to display at player ship position 
                pygame.display.update()                          # Call Update display function to show image
                enemy_spawn (enemy_list)                         # restart level & respawn wave of 10 enemy spaceships 
                player_health = 100                              # new live started so reset health
                wait(2000)                                       # pause game when live is lost

            if event.type == PLAYER_HIT:                         # player hit user configurable event detected
                player_health -= 20                              # reduce health by 20

            if player_health == 0 and player_lives > 0:          # when health reaches 0 AND Player still has lives
                player_lives -= 1                                # then remove a player live
                WIN.blit(spaceship_destroyed, (player_position)) # Set ship destroyed image to display at player ship position
                pygame.display.update()                          # Call Update display function to show image
                player_health = 100                              # reset player health for new live
                wait(2000)                                       # pause game when live is lost

            ### Player missile firing ###
            if event.type == pygame.KEYDOWN:        #player fires using spacebar (holding down does not fire multiple)
                if event.key == pygame.K_SPACE and len(player_missile) < MAX_NO_OF_MISSILES -1: 
                    missile = pygame.Rect(player_position.x + 2, player_position.y + 12, 2, 10) #missile fired from left image gun
                    player_missile.append(missile)  #missile loaded into list for tracking
                    player_shot_sound.play()        #play missile fired sound
                    missile = pygame.Rect(player_position.x + SCALE_WIDTH - 3, player_position.y + 12, 2, 10) #missile from right image gun
                    player_missile.append(missile)  #missile loaded into list for tracking
                    player_shot_sound.play()        #play missile fired sound

        key_pressed = pygame.key.get_pressed()              #check for a key pressed by user
        player_movement (key_pressed, player_position)      # call player_position function to move spaceship, passing parameters named

        enemy_movement (enemy_list, enemy_missile, level)   #call enemy movement function to move enemies acroos and down the screen
        
        enemy_missile_handling(enemy_list, enemy_missile, level) # call enemy missile handling function
        
        collision_handling (player_missile, enemy_missile, player_position, enemy_list) # call missile_handling function to track missiles, passing parameters named
        
        display_update (player_position, player_missile, enemy_missile, enemy_list, player_score, player_health, player_lives, high_score, level)  # call display_update function to refresh display window, passing parameters named

    pygame.quit() # call pygame quit function to close window and stop program

start_screen()  # call Game Start function
###########################################################################################################################################
