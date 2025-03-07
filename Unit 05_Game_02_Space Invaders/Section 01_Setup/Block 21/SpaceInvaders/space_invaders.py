import pygame, random

#Intialize pygame
pygame.init()

#Set Display Surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


class Game:
    """A class to help control and update gameplay"""

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        #Set game values
        self.round_number = 1
        self.score = 0
        # TODO: set the player to self.player
        # TODO: repeat for alien_group, player_bullet_group, alien_bullet_group.  set all to a self. version.

        #Set sounds and music
        self.new_round_sound = pygame.mixer.Sound("./assets/audio/new_round.wav")
        #TODO: repeat for breach_sound (using self) breach.wav
        #TODO: (cont.) alien_hit_sound to alien_hit.wav
        #TODO: (cont.) player_hit_sound to player_hit.wav

        #Set font
        self.font = pygame.font.Font("Facon.ttf", 32)

    def update(self):
        """Update the game"""
        ... #TODO: we will do this one later.

    def draw(self):
        """Draw the HUD and other information to display"""
        ... #TODO: we will do this one later.

    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse direction"""
        ... #TODO: we will do this one later.

    def check_collision(self):
        """Check for collisions"""
        ... #TODO: we will do this one later.

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""
        ... #TODO: we will do this one later.

    def start_new_round(self):
        """Start a new round"""
        ... #TODO: we will do this one later.

    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
        ... #TODO: we will do this one later.

    def pause_game(self, main_text, sub_text):
        """Pauses the game"""
        ... #TODO: we will do this one later.


    def reset_game(self):
        """Reset the game"""
        ... #TODO: we will do this one later.



