import pygame


class HeroPlane(object):  # 定义自己
    def __init__(self, screen): # 构造方法
        self.x = 190 # 定义默认 X 轴坐标
        self.y = 550 # 定义默认 y 轴坐标
        self.screen = screen
        self.image_name = "./Resources/my.png"
        self.image = pygame.image.load(self.image_name).convert_alpha() # 从本地加载图片并保留透明度

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

class EnemyPlane(object): # 定义敌机
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.image_name = "./Resources/enemy.png"
        self.image = pygame.image.load(self.image_name).convert_alpha() # 从本地加载图片并保留透明度
        self.direction = "right" # 默认移动方向
    
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):

        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2
        if self.x > 480 - 80:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"