import pygame


class CustomButton:

    def __init__(self, ss_game,image):
        self.settings = ss_game.settings
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = image

        self.rect = image.get_rect()
        self.rect.center = self.screen_rect.center
        



    def draw_custom_button(self):
        self.screen.blit(self.image, self.rect)

    def check_collison(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
