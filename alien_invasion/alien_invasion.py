import pygame
import game_functions as gf
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


class Settings():  # 设置类
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 初始化屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)

    stats = GameStats(ai_settings)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏
    while True:
        gf.check_events(ai_settings, stats, aliens, screen, ship, bullets, play_button)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets)

        gf.update_screen(ai_settings, stats, screen, ship,
                         aliens, bullets, play_button)


run_game()
