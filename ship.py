import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class for ship """

    def __init__(self, ai_game):
        """initialise the ship and set its starting point """
        super().__init__()
        self.screen = ai_game.screen
        self.temp = ai_game
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting
        self.image = pygame.image.load('alien_final.bmp')
        self.ship_rect = self.image.get_rect()
        self.rect = self.ship_rect
        self.ship_rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = float(self.ship_rect.x)
        self.y = float(self.ship_rect.y)

    def update(self):
        """update the ship's moving position based on moving flag"""
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        print(self.screen_rect.right)
        if self.moving_left and self.ship_rect.left > 0:
            self.x -= self.setting.ship_speed
        # update the ship position
        self.ship_rect.x = self.x
        if self.moving_up and self.ship_rect.top > 0:
            self.y -= self.setting.ship_speed
        if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed
        self.ship_rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.ship_rect)

    def center_ship(self):
        """Center the ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
