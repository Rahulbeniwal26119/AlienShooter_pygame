import sys

import pygame
import pygame.font


class Button:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.height, self.width = 50, 300
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  #prepaing the attribute for randering text
        self.rect = pygame.Rect(0, 0, self.width, self.height) #creating the rectangle object to place it on the screen
        self.rect.center = self.screen_rect.center #setting the rectangle element to the center on the screen
        self._prep_msg("Play")

    def _prep_msg(self, message):
        self.msg_image = self.font.render("Play", True, self.text_color, self.button_color) #creating a text image of text_color and button color
        self.msg_image_rect = self.msg_image.get_rect() # getting a rectangle element from the msg_image
        self.msg_image_rect.center = self.rect.center #pasting the text rectangle on the rect

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect) #use to fill the color into the rect attribute
        self.screen.blit(self.msg_image, self.msg_image_rect) #use to built a image on screen


play_button = Button()
while (True):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            sys.exit()
        play_button.draw_button()
    pygame.display.flip()
