import pygame.font
class Button:
    def __init__(self , ai_game , msg):
        """initialise the play button"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set the dimensions of the button
        self.width , self.height = 200 , 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None , 48)

        #build the the button rect object and center it
        self.rect = pygame.Rect(0 , 0 , self.width , self.height)
        self.rect.center = self.screen_rect.center

        #button message need to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self , msg):
        """Turn msg into rendered image and center text on the button"""
        self.msg_image = self.font.render(msg , True , self.text_color , self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color , self.rect)
        self.screen.blit(self.msg_image , self.msg_image_rect)
