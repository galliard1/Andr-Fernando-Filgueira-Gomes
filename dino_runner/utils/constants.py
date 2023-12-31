import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "A KNIGHT`S STORY"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FONT_STYLE = [
    os.path.join(IMG_DIR,'Fonts/Aceking.ttf'),
    os.path.join(IMG_DIR,'Fonts/BLOODY.ttf')
]

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Sword.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'SHIELD'
SWORD_TYPE = 'SWORD'
MAGIC_SCROLL_TYPE = 'MAGIC SCROLL'

WARRIOR_RUN = [
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Run-1.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Run-2.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Run-3.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Run-4.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Run-5.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Run-6.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Run-7.png.png')),
]

WARRIOR_SLIDE = [
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Slide-1.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Slide-2.png.png'))
]

WARRIOR_JUMP = [
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Jump-1.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Jump-2.png.png')),   
]

WARRIOR_SWORD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Attack3-1.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Attack3-2.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Attack3-3.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Attack3-4.png.png')),
]

DEATH_ICON = [
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-1.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-2.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-3.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-4.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-5.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-6.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-7.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-8.png.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Warrior/Death-9.png.png')),
]

MAGIC_SCROLL = pygame.image.load(os.path.join(IMG_DIR, 'Other/icon12.png'))

MAIN_THEME = pygame.mixer.music.load("dino_runner/assets/OST/Main_theme.mp3")
SELECT_SOUND = pygame.mixer.Sound("dino_runner/assets/OST/select_sound_right.mp3")
YOU_DIED_SOUND = pygame.mixer.Sound("dino_runner/assets/OST/You_died.mp3")
SWORD_SOUND = pygame.mixer.Sound("dino_runner/assets/OST/Sword_slash.mp3")
