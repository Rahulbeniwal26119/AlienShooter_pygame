import sys
from time import sleep

import pygame

from bullet import Bullet
from button import Button
from enemy import Enemy
from game_stat import GameStats
from scoreboard import ScoreBoard
from setting import Setting
from ship import Ship


class AlienAttack:
    """Overall class to manage game assests and characterstics of game"""

    def __init__(self):
        """Initialize the game , and create game resources"""
        pygame.init()
        self.setting = Setting()
        self.bullets = pygame.sprite.Group()  # use for collecting similar type of object
        self.screen = pygame.display.set_mode((0, 0),
                                              pygame.FULLSCREEN)  # 0 width and 0 length expresses the full screen
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        # pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.enemy = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.score_board = ScoreBoard(self)  #create a score board
        self._create_fleet()
        # as we need only one button then we need to call it once
        self.play_button = Button(self, "Play")

    def _create_fleet(self):
        """Create a fleet of alien"""

        new_enemy = Enemy(self)
        enemy_width, enemy_height = new_enemy.rect.size
        available_space_x = self.setting.screen_width - (2 * enemy_width)
        number_enemy_x = available_space_x // (2 * enemy_width)

        # determine the number of rows that will fit
        ship_height = self.ship.ship_rect.height
        available_space_y = self.setting.screen_height - (3 * enemy_height) - ship_height
        number_rows = available_space_y // (2 * enemy_height)

        # create a full fleet of aliens
        for row_number in range(number_rows + 1):
            for enemy_number in range(number_enemy_x + 1):
                self._create_alien(enemy_number, row_number)

    def _create_alien(self, enemy_number, row_number):
        new_enemy = Enemy(self)
        enemy_width, enemy_height = new_enemy.rect.size
        new_enemy.x = enemy_width + 2 * enemy_width * enemy_number
        new_enemy.rect.x = new_enemy.x
        new_enemy.rect.y = new_enemy.rect.height + 2 * new_enemy.rect.height * row_number
        self.enemy.add(new_enemy)

    def run_game(self):
        """Start the main loop for game"""
        while True:
            self._check_event()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_enemy()
            self._update_screen()

    def _ship_hit(self):
        """Respond to the ship being hit by alien"""
        # decrement ship left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.score_board.prep_ships()

            # get rid of any remaining aliens and bulllets
            self.enemy.empty()
            self.bullets.empty()

            # Create a new fleet
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.stats.reset_stat()
            self.ship.center_ship()
            pygame.mouse.set_visible(True)
            self.stats.level=  0

    def _update_enemy(self):
        """Update the position of enemy ships"""
        self._check_fleet_edges()
        self.enemy.update()
        # Look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.enemy):  # use for collision bw images or rectangles
            self._ship_hit()
        self._check_enemy_bottom()

    def _check_fleet_edges(self):
        """Respond appropriatly if any aliens have reached an edge"""
        for enemy in self.enemy.sprites():
            if enemy.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for enemy in self.enemy.sprites():
            enemy.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def _update_bullets(self):
        self.bullets.update()

        # get rid of the bullets that have disapperead
        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_enemy_collision()

    def _check_bullet_enemy_collision(self):
        """Respond to bullet - alien collision"""
        # check for any bullet that have hit enemy
        # if so , get rid of the bullet and the enemy
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemy, True, True)
        if not self.enemy:
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()

            #increase level
            self.stats.level+=1
            self.score_board.prep_level()
        if collisions:
            for enemy in collisions.values():
                self.stats.score+=self.setting.enemy_point * len(enemy)
            self.score_board.prep_score()
            self.score_board.check_high_score()

    def _check_event(self):
        """Response to keypress and mouse event"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicked clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stat()
            self.score_board.prep_score()
            self.setting.initialize_dynamic_setting()
            self.stats.game_active = True
            self.score_board.prep_level()
            pygame.mouse.set_visible(False)
            self.score_board.prep_ships()
            # Get rid of any remaining aliens and bullets
            self.enemy.empty()
            self.bullets.empty()


            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        """Response to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.setting.bullet_alloewed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_event(self, event):
        """Response to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemy.draw(self.screen)
        self.score_board.show_score()
        # draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        """Make the latest change visible on screen"""
        pygame.display.flip()

    def _check_enemy_bottom(self):
        """check if any aliens have reached the bottom of screen"""
        screen_rect = self.screen.get_rect()
        for enemy in self.enemy.sprites():
            if enemy.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    ai = AlienAttack()
    ai.run_game()
