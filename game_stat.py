class GameStats:
    """Track statstics for Alien Invasion"""

    def __init__(self , ai_game):
        self.setting = ai_game.setting
        #start alien invasion in active state
        self.game_active = False # make it True on clicking on play button
        self.reset_stat()
        self.high_score = 0
        self.score = 0
        self.level = 1

    def reset_stat(self):
        """initialize statstics that can change during the game"""
        self.ships_left = self.setting.ship_limit
        self.score = 0
