import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for managing the bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        # Create a bullet rectangle at (0 , 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.ship_rect.midtop

        # store the bullet position at a decimal value
        self.y = int(self.rect.y)

    def update(self):
        """Move the bullet upward"""
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
