import pygame

class Settings:

    def __init__(self):

        #Background settings
        self.load_image = pygame.image.load('images/scp_261_background.png')
        self.background_image = pygame.transform.scale(self.load_image, (1200,800))

        self.bg_width = 1200
        self.bg_height = 800
        
        self.menu_bg = (0,150,0)
        #Button Images
        self.button_size = (250,90)
        self.load_play_button = pygame.image.load('images/play_button.png')
        self.play_button_image = pygame.transform.scale(self.load_play_button, self.button_size)
        self.play_button_rect = self.play_button_image.get_rect()

        self.load_quit = pygame.image.load('images/quit_button.png')
        self.quit_image = pygame.transform.scale(self.load_quit, self.button_size)

        self.load_back = pygame.image.load('images/back_button.png')
        self.back_image = pygame.transform.scale(self.load_back, self.button_size)

        self.load_save = pygame.image.load('images/new_save.png')
        self.save_image = pygame.transform.scale(self.load_save,self.button_size)
        #Scp 261 settings
        self.machine_width = 180
        self.machine_height = 360
        #Invetory
        self.inv_height = 200
        self.inv_width = 800
        self.items = []

        self.inv_slot_w,self.inv_slot_h = 100,80
        #Cash
        self.cash = 200
        self.cash_added = 50
        self.cashb_width = 100
        self.cashb_height = 50
        #Health
        self.hp = 300
        #Item images
        self.load_dd = pygame.image.load('images/diet_dark.png')
        self.load_dg = pygame.image.load('images/diet_ghost.png')
        self.load_dz = pygame.image.load('images/diet_zero.png')
        self.load_dt = pygame.image.load('images/dragon_twist.png')

        self.diet_dark = pygame.transform.scale(self.load_dd,(self.inv_slot_w,self.inv_slot_h))
        self.diet_ghost = pygame.transform.scale(self.load_dg,(self.inv_slot_w,self.inv_slot_h))
        self.diet_zero = pygame.transform.scale(self.load_dz,(self.inv_slot_w,self.inv_slot_h))
        self.dragon_twist = pygame.transform.scale(self.load_dt,(self.inv_slot_w,self.inv_slot_h))

        self.damage_taken = 299


        #Effect text
        self.effect_text = "The machine looks paranormal"

        #Achievements
        self.ghost_drank = 0
        self.achievement_size = (125,45)
        self.cash_achievement = False
        self.hp_achievement = False
        self.ghost_achievement = False



    def reset_game(self):
        self.effect_text = "The machine looks pananormal"
        self.cash = 100
        self.items.clear()
        self.hp = 300
        self.menu_bg = (0,150,0)
        self.ghost_drank = 0
        
        
