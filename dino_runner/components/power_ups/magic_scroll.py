import pygame

from dino_runner.utils.constants import MAGIC_SCROLL,MAGIC_SCROLL_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class MagicScroll(PowerUp):
    def __init__(self):
        self.image = MAGIC_SCROLL
        self.image = pygame.transform.scale(self.image,(32*2,32*2))
        self.type = MAGIC_SCROLL_TYPE
        super().__init__(self.image,self.type)