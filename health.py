import pygame
from text import Text


class HealthBar:

    def __init__(self, ss_game):
        self.settings = ss_game.settings
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        
        self.health = pygame.Rect(0,0,self.settings.hp,35)
        self.health.midbottom = self.screen_rect.midbottom
        self.color = (0,250,0)
    def draw_hp(self):
        pygame.draw.rect(self.screen,self.color,self.health)

    def create_hp_text(self):
        self.text = Text(self, str(self.settings.hp))
        self.text.text_color = (255,255,255)
        self.text.bg_color = (0,250,0)
        self.text.make_text()
        self.text.text_rect.midbottom = self.screen_rect.midbottom
        self.text.draw_text()
    def update_rect(self):
        self.health.update(0,0,self.settings.hp,35)
        self.create_hp_text()
        self.health.midbottom = self.screen_rect.midbottom
        
