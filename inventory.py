import pygame
    

class Inventory:

    def __init__(self, ss_game):
        self.settings = ss_game.settings
        self.cash_button = ss_game.cash_button
        
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.load_image = pygame.image.load('images/inventory.png')
        self.image = pygame.transform.scale(self.load_image, (self.settings.inv_width, self.settings.inv_height))

        self.items = self.settings.items

        self.items_total = pygame.sprite.Group()
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.draw_inv = False
        self.x = 225
        self.dark_side = True
        
    def draw_inventory(self):
        self.rect.y = 125
        self.screen.blit(self.image, self.rect)


           
    def check_inv(self):
        return self.draw_inv
        
    def create_slots(self):
        #x = 250 y = 365
        cur_x = 250
        for item in self.settings.items:
            item.draw_item(cur_x,190)
            self.items_total.add_internal(item)
            cur_x += 200
            


    def inv_slot_collison(self):
        for item in self.settings.items:
            if item.check_slot_collison():
                if item.image == self.settings.dragon_twist:
                    self.settings.hp += 150
                    self.settings.effect_text = "The drink tastes like dragon fruit"
                if item.image == self.settings.diet_dark:
                    self.darkside_effect()
                if item.image == self.settings.diet_zero:
                    self.settings.hp -= 0
                    self.settings.effect_text = "The drink tasted like nothing"
                if item.image == self.settings.diet_ghost:
                    self.settings.ghost_drank += 1
                    self.settings.hp -= self.settings.damage_taken
                    self.settings.effect_text = "You start to feel the presence of a ghost"
                self.settings.items.remove(item)
    
    
            
            
    def darkside_effect(self):
        if self.dark_side:
            self.settings.menu_bg = (0,0,0)
            self.cash_button.bg_color = (0,0,0)
            self.settings.effect_text = "Everything seems dark"
            self.dark_side = False
        elif not self.dark_side:
            self.settings.menu_bg = (0,150,0)
            self.cash_button.bg_color = (0,150,0)
            self.settings.effect_text = "Everything seems seems normal again"
            self.dark_side = True
            
            
            
