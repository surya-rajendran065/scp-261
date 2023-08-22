import pygame



class Machine:

    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.load_image = pygame.image.load('images/scp_261_image.png')
        self.image = pygame.transform.scale(self.load_image, (self.settings.machine_width, self.settings.machine_height))
        self.rect = self.image.get_rect()

    def draw_machine(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.screen.blit(self.image, self.rect)
        
    def check_collison(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
        
