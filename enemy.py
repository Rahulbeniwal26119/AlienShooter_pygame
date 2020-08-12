import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """initialise the alien an set its starting position"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set it
        self.image = pygame.image.load('opposite_alien.bmp')
        self.rect = self.image.get_rect()

        # start each alien from the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens exact horizontal position
        self.x = float(self.rect.x)
        self.setting = ai_game.setting
        
    def update(self):
        """Move the alien to the right"""
        self.x += (self.setting.enemy_speed * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        """Return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True
