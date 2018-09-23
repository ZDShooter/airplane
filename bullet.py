import pygame


class Bullet(object):
    def __init__(self, x, y, screen):
        global hero_image
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        hero_image = pygame.image.load("./Resources/bullet1.png").convert_alpha()

    def display(self):
        self.screen.blit(hero_image, (self.x, self.y))

    def move(self):
        self.y -= 2

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(object):
    def __init__(self, x, y, screen):
        global enemy_image
        self.x = x + 30
        self.y = y + 30
        self.screen = screen
        enemy_image = pygame.image.load("./Resources/bullet2.png").convert_alpha()

    def display(self):
        self.screen.blit(enemy_image, (self.x, self.y))

    def move(self):
        self.y += 2

    def judge(self):
        if self.y > 700:
            return True
        else:
            return False