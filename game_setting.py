### Define & Change Game CONSTANT Variables ############################

### Game window title ###
GAME_TITLE = "Space Invaders - George Hand"    # Game Title to display in window header

### High score file name ###
HIGH_SCORE_FILE = "high_score.txt"        # name of high score file

### Display settings ###
WINDOW_WIDTH, WINDOW_HEIGHT = 1400, 800   # defining screen size constant variables
SCALE_WIDTH, SCALE_HEIGHT = 55, 55        # scale image files to display appropriate size on in the game
DISPLAY_UPDATE_SPEED_FPS = 60             # set update speed to 60 frames per second so the game will run the same on all computers/machines
GAME_TEXT_Y_POS = 15                      # Y Position of all game text - scores, lives, hi-scores
HEALTH_BAR_X_POS = 900                    # X Position of Health Bar
TEXTBOX_X, TEXTBOX_Y  = 360, 180          # Gameover text box position x & y
TEXTBOX_WIDTH, TEXTBOX_HEIGHT = 700, 100  # Gameover text box width & height

### Base speeds ###
PLAYER_VELOCITY = 4                       # set player spaceship movement speed
ENEMY_VELOCITY = 2                        # set enemy spaceship movement speed
MISSILE_VELOCITY = 5                      # set missile speed

### Max values ###
MAX_NO_OF_MISSILES = 6                    # set maximum number of missile at one time, stop player firing contiuously for better game play
MAX_ENEMY_MISSILES = 4                    # set starting max number of enemy missiles....add to each level as player improves

### Base score values ###
PLAYER_HIT_HEALTH_LOSS = 20               # set percentage loss each time player is hit
ENEMY_KILL_VALUE = 10                     # Score for killing an enemy

### define colours used in RGB scale ###
WHITE = (255,255,255)                     # set RGB (Red, Green, Blue) colour - White
RED = (255, 0 , 0)                        # set RGB (Red, Green, Blue) colour - Red
GREEN = (0, 255, 0)                       # set RGB (Red, Green, Blue) colour - Green
YELLOW = (255, 255, 0)                    # set RGB (Red, Green, Blue) colour - Yellow
GREY = (128, 128,128)                     # set RGB (Red, Green, Blue) colour - Grey
AMBER = (255, 191, 0)                     # set RGB (Red, Green, Blue) colour - Amber
