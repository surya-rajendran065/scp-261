import pygame

class Achievement:

    def __init__(self, ss_game):
        self.settings = ss_game.settings
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        self.load_image = pygame.image.load('images/star.png')
        self.image = pygame.transform.scale(self.load_image, self.settings.achievement_size)
        self.rect = self.image.get_rect()

    def draw_achievement(self, x_pos=0, y_pos=0):
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.screen.blit(self.image,self.rect)