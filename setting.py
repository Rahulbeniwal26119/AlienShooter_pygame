class Setting:
    """A class to store all setting for alien invasion"""

    def __init__(self):
        """initialise the game static  setting"""
        self.screen_width = 1200  # as the screen_width changed from the AlienAttack __init__ method
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (225, 225, 225)
        self.bullet_alloewed = 3
        self.fleet_drop_speed = 60
        self.bullet_speed = 1.5
        self.ship_limit = 2  # work as 3
        self.score_scale = 1.5  # for changing the point values

        # how quickly the game speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """providing the first time value to those attributes that can be changed"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.enemy_speed = 1.0

        # fleet direction one represent right , - represent -1
        self.fleet_direction = 1
        self.enemy_point = 10

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale
        self.enemy_point = int(self.enemy_point * self.score_scale)
        print(self.enemy_point)