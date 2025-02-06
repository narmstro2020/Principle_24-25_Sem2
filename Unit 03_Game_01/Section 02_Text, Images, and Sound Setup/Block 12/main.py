import random, pygame

pygame.init()

# TODO: we need some constants.  WINDOW_WIDTH and WINDOW_HEIGHT, 800, 600
# TODO: create display_surface assign to it pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# TODO: call pygame.display.set_caption()  and pass in the argument "Burger Dog"

# TODO: create an FPS variable and assign 60 to it.
# TODO: create a clock variable and assign pygame.time.Clock()

# TODO: we need the following constants
# TODO: PLAYER_STARTING_LIVES, PLAYER_NORMAL_VELOCITY, PLAYER_BOOST_VELOCITY, STARTING_BOOST_LEVEL
# TODO: STARTING_BURGER_VELOCITY, BURGER_ACCELERATION, BUFFER_DISTANCE
# TODO: values of these variables are: 3, 5, 10, 100, 3, 0.5, 100

score = 0
burger_points = 0
burgers_eaten = 0


# TODO: create a player_lives variable and assign PLAYER_STARTING_LIVES to it
# TODO: create a player_velocity variable and assign PLAYER_NORMAL_VELOCITY to it
# TODO: create a boost_level variable and assign STARTING_BOOST_LEVEL to it
# TODO: create a burger_velocity variable and assign STARTING_BURGER_VELOCITY to it

# TODO: 3 colors, ORANGE, BLACK, AND WHITE.  BLACK and WHITE are standard RGB, ORANGE is a tuple (246, 170, 54)
# TODO: please note the colors are tuples.

# TODO: create a font variable and assign pygame.font.Font() passing in "WashYourHand.ttf", 32

# NOTES:  text is a str, background_color is a tuple[int, int, int]
# NOTES:  **locations is basically a dictionary of str, tuple[int, int] or int
# NOTES:  this prep_text returns a tuple containing a Font object and a Rectangle object.
def prep_text(text: str, background_color: tuple[int, int, int], **locations):
    # TODO: create a text_to_return variable and assign font.render(text, True, background_color)
    # TODO: create a rect variable and assign text_to_return.get_rect()
    # TODO: create a for location in locations loop
    # TODO: for loop block start
    if location == "topleft":
        rect.topleft = locations["topleft"]
    elif location == "centerx":
        rect.centerx = locations["centerx"]
    # TODO: (2025-02-06): add this elif portion
    elif location = "y":
        rect.y = locations["y"]
    # TODO: (2025-02-06): add this elif portion
    elif location = "topright"
    rect.topright = locations["topright"]

# TODO: (2025-02-06): add this elif portion
elif location = "center"
rect.center = locations["center"]
# NOTE:  We'll add more later.
# TODO: for loop block end
# TODO: return (text_to_return, rect)
pass  # TODO: remove this when done.

# Set Text Blocks
# TODO: (2025-02-06): assign to (points_text, points_rect)
# TODO: (continued): the result of the call to prep_text() given f"Burger Points: {burger_points}", ORANGE,
# TODO: (continued): topleft=(10, 10)

# TODO: (2025-02-06): assign to (score_text, score_rect)
# TODO: (continued): the result of the call to prep_text() given f"Score: {score}", ORANGE,
# TODO: (continued): topleft=(10, 50)

# TODO: (2025-02-06): assign to (title_text, title_rect)
# TODO: (continued): the result of the call to prep_text() given "Burger Dog", ORANGE,
# TODO: (continued): centerx=WINDOW_WIDTH // 2, y=10

# TODO: (2025-02-06): assign to (eaten_text, eaten_rect)
# TODO: (continued): the result of the call to prep_text() given f"Burgers Eaten: {burgers_eaten}", ORANGE,
# TODO: (continued): centerx=WINDOW_WIDTH // 2, y=50

# TODO: (2025-02-06): assign to (lives_text, lives_rect)
# TODO: (continued): the result of the call to prep_text() given f"Lives: {player_lives}", ORANGE,
# TODO: (continued): topright=(WINDOW_WIDTH - 10, 10)

# TODO: (2025-02-06): assign to (boost_text, boost_rect)
# TODO: (continued): the result of the call to prep_text() given f"Boost: (boost_level)", ORANGE,
# TODO: (continued): topright=(WINDOW_WIDTH - 10, 50)

# TODO: (2025-02-06): assign to (game_over_text, game_over_rect)
# TODO: (continued): the result of the call to prep_text() given f"FINAL SCORE: {score}", ORANGE,
# TODO: (continued): center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT //2)

# TODO: (2025-02-06): assign to (continue_text, continue_rect)
# TODO: (continued): the result of the call to prep_text() given "Press any key to play again", ORANGE,
# TODO: (continued): center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT //2 + 64)

# Set sounds and music
# TODO: (2025-02-06): create a bark_sound variable and assign pygame.mixer.Sound() passing in "bark_sound.wav"
# TODO: (2025-02-06): create a miss_sound variable and assign pygame.mixer.Sound() passing in "miss_sound.wav"
# TODO: (2025-02-06): call pygame.mixer.music.load() passing in "bd_background_music.wav"

# Set images
# TODO: (2025-02-06): create a player_image_right variable and assign pygame.image.load() passing in "dog_right.png"
# TODO: (2025-02-06): create a player_image_left variable and assign pygame.image.load() passing in "dog_left.png"

player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.bottom = WINDOW_HEIGHT

# TODO: (2025-02-06): create a burger_image variable and assign pygame.image.load() passing in "burger.png"
# TODO: (2025-02-06): create a burger_rect variable and aassign from burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)














