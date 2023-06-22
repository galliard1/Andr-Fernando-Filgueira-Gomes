import pygame

from dino_runner.utils.constants import BG,SELECT_SOUND, ICON,DEATH_ICON,MAGIC_SCROLL_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,FONT_STYLE,DEFAULT_TYPE
from dino_runner.components.dinosaur import Warrior
from dino_runner.components.clouds import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0

        self.player = Warrior()
        self.cloud = Cloud()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.playing = True     
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.update()
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)
    
    def update_score(self):
        self.score += 1
        if self.player.type == MAGIC_SCROLL_TYPE:
            self.game_speed = 20
        if self.score % 100 == 0:                
            self.game_speed += 3
                

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((218, 218, 218))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.draw_text(f'SCORE: {self.score}', (1000,50))
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.draw_text(f'{self.player.type.capitalize()} ENABLED FOR {time_to_show} SECONDS',(500,50))
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_text(self,
                  text,text_rect,
                  font_size=35,
                  font_style = FONT_STYLE[0],
                  font_color = (195,161,24)
                  ):
        font = pygame.font.Font(font_style, font_size)
        self.text = font.render(f'{text}', True, (font_color))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = text_rect
        self.screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                SELECT_SOUND.play()
                self.run()

    def show_menu(self):
        self.screen.fill((0,0,0))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.draw_text('PRESS ANY KEY TO START',(half_screen_width,half_screen_height))
           
        else:
            self.image = DEATH_ICON[8]
            self.image = pygame.transform.scale(self.image,(187*2,137*2))
            self.screen.blit(self.image, (half_screen_width-133,half_screen_height-340))
            self.draw_text('YOU DIED', (half_screen_width,half_screen_height-20),60,FONT_STYLE[1],(255,0,0))
            self.draw_text('PRESS ANY KEY TO RESTART', (half_screen_width,half_screen_height+50))
            self.draw_text(f'YOUR SCORE WAS: {self.score}',(half_screen_width,half_screen_height+100))
            self.draw_text(f'YOUR DEATH COUNT IS: {self.death_count}',(half_screen_width,half_screen_height+150))
            self.game_speed = 20
            pygame.mixer.music.fadeout(500)

        pygame.display.update()

        self.handle_events_on_menu()
    

