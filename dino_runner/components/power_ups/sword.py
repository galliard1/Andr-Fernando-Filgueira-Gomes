import pygame

from dino_runner.utils.constants import SWORD, SWORD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Sword(PowerUp):
    def __init__(self):
        self.image = SWORD
        self.image = pygame.transform.scale(self.image,(32*2,32*2))
        self.type = SWORD_TYPE
        super().__init__(self.image,self.type)