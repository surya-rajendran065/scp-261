import pygame
from pygame.font import SysFont


class Text:

    def __init__(self, ss_game, msg):
        self.settings= ss_game.settings
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.msg = msg

        self.bg_color = self.settings.menu_bg
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)
        self.make_text()

    def make_text(self):
        self.text = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.text_rect = self.text.get_rect()
        
    def draw_text(self):
        self.screen.blit(self.text,self.text_rect)
    def text_collison(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.text_rect.collidepoint(mouse_pos)

