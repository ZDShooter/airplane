import pygame # 导入 Pygame 模块
from plane import * # 导入本地 plane 模块
import time # 导入 time 模块
from pygame.locals import *


def start(): # 定义一个 start 类
    screen = pygame.display.set_mode((480, 700))
    background = pygame.image.load("./Resources/background.png").convert()
    hero_plane = HeroPlane(screen)
    enemy_plane = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        hero_plane.display()
        enemy_plane.move()
        enemy_plane.launch_bullet()
        enemy_plane.display()
        time.sleep(0.01)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                print("再见")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    print("←")
                    hero_plane.move_left()
                if event.key == K_RIGHT or event.key == K_d:
                    print("→")
                    hero_plane.move_right()
                if event.key == K_SPACE:
                    print("你按了空格")
                    hero_plane.launch_bullet()

if __name__ == '__main__':
    start()
