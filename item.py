import pygame
from pygame.sprite import Sprite

class Item(Sprite):
    def __init__(self,ss_game, image):
        self.settings = ss_game.settings
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.image = image
        self.image_rect = self.image.get_rect()
        self.y = 100
        self.x = 225
        self.darkside_effect = False
        

    def draw_item(self, x_pos, y_pos):
        self.image_rect.x = x_pos
        self.image_rect.y = y_pos
        self.screen.blit(self.image,self.image_rect)

    def check_slot_collison(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.image_rect.collidepoint(mouse_pos)
    def check_darkside(self):
        return self.dakrside_effect
    def darkside_effects(self):
        self.settings.menu_bg = (0,0,0)

    
    
        


    

        