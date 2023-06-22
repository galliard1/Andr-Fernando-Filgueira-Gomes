import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import MAGIC_SCROLL_TYPE,WARRIOR_SWORD ,WARRIOR_RUN, WARRIOR_SLIDE, DEFAULT_TYPE, SHIELD_TYPE,SWORD_TYPE,WARRIOR_JUMP

X_POS = 80
Y_POS = 250
Y_POS_SLIDE = 245
JUMP_VEL = 8.5

DUCK_IMG = {
    DEFAULT_TYPE: WARRIOR_SLIDE, 
    SHIELD_TYPE: WARRIOR_SLIDE,
    SWORD_TYPE: WARRIOR_SLIDE,
    MAGIC_SCROLL_TYPE: WARRIOR_SLIDE  
    }
JUMP_IMG = {
    DEFAULT_TYPE: WARRIOR_JUMP, 
    SHIELD_TYPE: WARRIOR_JUMP,
    SWORD_TYPE: WARRIOR_JUMP,
    MAGIC_SCROLL_TYPE: WARRIOR_JUMP 
    }
RUN_IMG = {
    DEFAULT_TYPE: WARRIOR_RUN, 
    SHIELD_TYPE: WARRIOR_RUN, 
    SWORD_TYPE: WARRIOR_SWORD,
    MAGIC_SCROLL_TYPE: WARRIOR_RUN    
    }


class Warrior(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.warrior_rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.warrior_rect.x = X_POS
        self.warrior_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.warrior_run = True
        self.warrior_jump = False
        self.warrior_slide = False
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show__text = False
        self.has_power_up_time = 0
    
    def update(self,user_input):
        if self.warrior_run:
            self.run()
        elif self.warrior_jump:
            self.jump()
        elif self.warrior_slide:
            self.slide()

        if user_input[pygame.K_UP] or user_input[pygame.K_SPACE] and not self.warrior_jump:
            self.warrior_jump = True
            self.warrior_run = False
            self.warrior_slide = False
        elif not self.warrior_jump:
            self.warrior_jump = False
            self.warrior_run = True
            self.warrior_slide = False
        if user_input[pygame.K_DOWN] and not self.warrior_jump:
            self.warrior_slide = True
            self.warrior_jump = False
            self.warrior_run = False

        if self.step_index >= 20:
            self.step_index = 0
        
    # warrior running
    def run(self):
        if self.type == SWORD_TYPE:
            self.image = RUN_IMG[self.type][self.step_index//5]
        else:
            self.image = RUN_IMG[self.type][self.step_index//3]

        self.image = pygame.transform.scale(self.image,(187*1.2,137*1.2))
        self.warrior_rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.warrior_rect.x = X_POS
        self.warrior_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = WARRIOR_JUMP[0] if self.step_index <10 else WARRIOR_JUMP[1] 
        self.image = pygame.transform.scale(self.image,(187*1.3,137*1.3))
        self.mask = pygame.mask.from_surface(self.image)
        self.step_index += 1
        if self.warrior_jump:
            self.warrior_rect.y -= self.jump_vel *4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.warrior_rect.y = Y_POS
            self.warrior_jump = False
            self.jump_vel = JUMP_VEL
    
    # warrior slide
    def slide(self):
        self.image = WARRIOR_SLIDE[0] if self.step_index <10 else WARRIOR_SLIDE[1]
        self.image = pygame.transform.scale(self.image,(187*1.2,137*1.2))
        self.warrior_rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.warrior_rect.x = X_POS
        self.warrior_rect.y = Y_POS_SLIDE
        self.step_index += 1     
          
    def draw(self, screen):
        screen.blit(self.image, (self.warrior_rect.x, self.warrior_rect.y))