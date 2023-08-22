import pygame


class Button:

    def __init__(self, ss_game):
        self.settings = ss_game.settings
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
    
        self.load_image = pygame.image.load('images/play_button.png')
        self.image = pygame.transform.scale(self.load_image, self.settings.button_size)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center


    def draw_button(self):
        self.screen.blit(self.image,self.rect)
        
    def check_button(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

        
