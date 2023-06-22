import pygame
import random

from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS,DEFAULT_TYPE,YOU_DIED_SOUND,SWORD_SOUND, LARGE_CACTUS,BIRD, SHIELD_TYPE, SWORD_TYPE,MAGIC_SCROLL_TYPE


class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.mask.overlap(obstacle.mask,
                (obstacle.rect.x - game.player.warrior_rect.x, 
                 obstacle.rect.y - game.player.warrior_rect.y)):
                if not game.player.has_power_up or game.player.type == MAGIC_SCROLL_TYPE:
                    pygame.time.delay(500)
                    game.player.has_power_up = False
                    game.playing = False
                    game.death_count += 1
                    YOU_DIED_SOUND.set_volume(0.5)
                    YOU_DIED_SOUND.play()
                    break
                elif game.player.type == SWORD_TYPE:
                    SWORD_SOUND.play()
                    self.obstacles.remove(obstacle)


    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)