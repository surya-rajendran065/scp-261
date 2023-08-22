import pygame
from pygame.sprite import Sprite
import sys
import time
import random
import json
from pathlib import Path



from settings import Settings
from machine import Machine
from play_button import Button
from button import CustomButton
from inventory import Inventory
from item import Item
from text import Text
from health import HealthBar
from achievement import Achievement



class scp_261:
    #important atrritbutes
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.bg_width,self.settings.bg_height))
        pygame.display.set_caption("Scp 261")
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.game_active = False
        self.Game_over = False
        self.screen_label = "menu"
        self.drinks = [self.settings.diet_dark,self.settings.diet_zero,self.settings.diet_ghost,self.settings.dragon_twist]
        self.load_data = True

        self.play_button = Button(self)
        self.play_button.rect.y = 225

        self.quit_button = CustomButton(self, self.settings.quit_image)
        self.quit_button.rect.y = self.play_button.rect.y + 200

        self.save_button = CustomButton(self, self.settings.save_image)
        self.save_button.rect.y = self.play_button.rect.y + 100

        self.back_button = CustomButton(self, self.settings.back_image)
        self.back_button.rect.y = 50
        self.back_button.rect.x = 890

        self.scp_261 = Machine(self)
        

        self.healthbar = HealthBar(self)
        
        

        self.title = Text(self, "Scp 261 game!")
        self.title.text_rect.midtop = self.screen_rect.midtop

        self.cash_button = Text(self, "Cash Button")
        self.cash_button.text_color = (255,255,255)
        self.cash_button.make_text()
        
        self.cash_ach = Achievement(self)
        self.health_ach = Achievement(self)
        self.ghost_ach = Achievement(self)

        self.draw_ach1 = False
        self.draw_ach2 = False
        self.draw_ach3 = False
        

        self.invetory_system = Inventory(self)
        self.text_str = self.settings.effect_text

    #Data
    def save_data(self):
        data = {
            "cash":self.settings.cash,
            "health":self.settings.hp,
            "cash_ach":self.settings.cash_achievement,
            "health_ach":self.settings.hp_achievement,
            "ghost_ach":self.settings.ghost_achievement
        }
        path = Path('game_data.json')
        my_data = data
        contents = json.dumps(my_data)
        path.write_text(contents)
    def check_data(self):
        path = Path('game_data.json')
        
        if path.exists() and self.load_data:
            read_text = path.read_text()
            load = json.loads(read_text)
            self.settings.cash = load["cash"]
            self.settings.cash_achievement = load["cash_ach"]
            self.settings.hp_achievement = load["health_ach"]
            self.settings.ghost_achievement = load["ghost_ach"]
            self.load_data = False
            
        
    #Events
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.check_button() and self.screen_label == "menu":
                    self.screen_label = "game"
                    
                if self.quit_button.check_collison() and self.screen_label == "menu": 
                    pygame.quit()
                    sys.exit()
                #Active game
                if self.back_button.check_collison() and self.screen_label == "game":
                   self.screen_label = "menu"

                if self.scp_261.check_collison() and self.screen_label == "game":
                    self.check_drink_list()
                    self.check_cash()
                if self.cash_button.text_collison() and self.screen_label == "game":
                    self.settings.cash += self.settings.cash_added
                if self.invetory_system.inv_slot_collison() and self.screen_label == "game":
                    print("You click")
                if self.save_button.rect.collidepoint(pygame.mouse.get_pos()) and self.screen_label == "menu":
                    self.save_data()
                    
                    
                
                
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
                
    def check_keydown_events(self, event):
        if event.key == pygame.K_TAB and self.screen_label == "game":
            if not self.invetory_system.draw_inv:
                self.invetory_system.draw_inv = True
            elif self.invetory_system.draw_inv:
                self.invetory_system.draw_inv = False
            

    #Inventory
    def check_invetory_system(self):
        if self.invetory_system.draw_inv:
            self.invetory_system.draw_inventory()
            self.invetory_system.create_slots()
            
            
    #Items
    def check_drink_list(self):
        if len(self.settings.items) < 4 and self.settings.cash != 0:
            self.generated_drink = random.choice(self.drinks)
            self.settings.items.append(Item(self, self.generated_drink))
          

    #Cash
    def draw_cash(self):
        cash_str = f"¥{self.settings.cash}"
        cash_display = Text(self, cash_str)
        cash_display.text_color = (255,255,255)
        cash_display.make_text()
        cash_display.text_rect.topright = self.screen_rect.topright
        cash_display.draw_text()

    def check_cash(self):
        if self.settings.cash > 0 and self.screen_label == "game":
            self.settings.cash -= 50
    
            
            
    #Text
    def make_effect_txt(self):
        text_str = self.settings.effect_text
        self.effect_button = Text(self, text_str)
        self.effect_button.text_color = (255,255,255)
        self.effect_button.make_text()
        self.effect_button.text_rect.midbottom = self.screen_rect.midbottom
        self.effect_button.text_rect.y = 50
        self.effect_button.draw_text()

        
    #Game Over
    def game_over(self):
        self.screen.fill((0,0,0))
        self.gameo_text = Text(self, "Game Over")
        self.gameo_text.text_color = (255,255,255)
        self.gameo_text.bg_color = (0,0,0)
        self.gameo_text.make_text()
        self.gameo_text.text_rect.center = self.screen_rect.center
        self.gameo_text.draw_text()
        time.sleep(2)
        self.settings.reset_game()
        self.cash_button.bg_color = (self.settings.menu_bg)
        self.screen_label = "menu"
        
        
        
            
        
        
    #Hp
    def check_hp(self):
        if self.settings.hp <= 0:
            self.screen_label = "game_over"
    #Achievements
    def check_achievements(self):
        if self.settings.cash > 10000:
            self.settings.cash_achievement = True
        if self.settings.hp > 1000:
            self.settings.hp_achievement = True
        if self.settings.ghost_drank >= 5:
            self.settings.ghost_achievement = True
        self.if_achive()
    def if_achive(self):
        if self.settings.cash_achievement:
            self.draw_ach1 = True
            self.settings.cash_added = 100
        if self.settings.hp_achievement:
            self.draw_ach2 = True
            for i in range(1):
                if self.settings.hp == 300:
                    self.settings.hp += 50
                break
        if self.settings.ghost_achievement:
            self.settings.damage_taken = 250
            self.draw_ach3 = True
    def drawing_ach(self):
        if self.draw_ach1:
            self.cash_ach.draw_achievement(0,0)
        if self.draw_ach2:
            self.health_ach.draw_achievement(0,45)
        if self.draw_ach3:
            self.ghost_ach.draw_achievement(0,90)


            
            

            
    #Screen and Game
    def update_screen(self):
        if self.screen_label == "menu":
            self.main_menu()
        
            
        pygame.display.flip()
        self.clock.tick(60)

    def run_game_elements(self):
        self.screen.blit(self.settings.background_image,(0,0))
        self.cash_button.make_text()
        self.scp_261.draw_machine(500,350)
        self.back_button.draw_custom_button()
        self.check_invetory_system()
        self.draw_cash()
        self.make_effect_txt()
        self.cash_button.make_text()
        self.cash_button.draw_text()
        self.healthbar.draw_hp()
        self.healthbar.update_rect()
        
        
        self.check_hp()
        
        
        
    def main_menu(self):
        self.check_data()
        self.screen.fill(self.settings.menu_bg)
        self.play_button.draw_button()
        self.quit_button.draw_custom_button()
        self.save_button.draw_custom_button()
        self.title.draw_text()
        self.check_achievements()
        self.drawing_ach()
        
        
        

    def run_game(self):
        while True:
            self.check_events()
            if self.screen_label == "game":
                self.check_data()
                self.run_game_elements()
            elif self.screen_label == "game_over":
                self.game_over()
            self.update_screen()
            

if __name__ == '__main__':
    game = scp_261()
    game.run_game()