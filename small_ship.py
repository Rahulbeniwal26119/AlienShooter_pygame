import pygame
from pygame.sprite import Sprite
class SmallShip(Sprite):
    """class for displaying ships left"""
    def __init__(self, ai_game):
        super().__init__()
        self.image = pygame.image.load("alien_final_small.bmp")
        self.rect  = self.image.get_rect()
