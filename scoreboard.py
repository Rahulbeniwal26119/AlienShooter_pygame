import pygame.font
from pygame.sprite import Group
from ship import Ship
from small_ship import SmallShip


class ScoreBoard:
    """A class to report the score"""

    def __init__(self, ai_game):
        """initialize the scorekeeping attributes"""
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting
        self.stats = ai_game.stats

        # font setting for score
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into rendered image"""

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)

        # display the score at the top left of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        # self.screen_rect.top = 20
        self.score_rect.y = 10

    def prep_high_score(self):
        """Turn the high score into a render image """
        high_score = round(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.setting.bg_color)

        # center the high score the top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str , True  , self.text_color , self.setting.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom + 10



    def show_score(self):
        """Draw scores , level , and the ships left to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image , self.level_rect)
        self.ships.draw(self.screen)

    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.stats.ships_left+1):
            ship = SmallShip(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 40
            self.ships.add(ship)