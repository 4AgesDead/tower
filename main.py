import pygame
import os
import sys
import random

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

from load import *
def restart():
    global bush_group, bush_tower_group, grass_group, right_group, left_group, up_group, down_group
    bush_group = pygame.sprite.Group()
    bush_tower_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    right_group = pygame.sprite.Group()
    left_group = pygame.sprite.Group()
    up_group = pygame.sprite.Group()
    down_group = pygame.sprite.Group()
class Bush(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class Bush_tower(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class Grass(pygame.sprite.Sprite):
    def __init__(self, image, pos)
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class Right(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class Up(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class Down(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class Left(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

def drawMaps(nameFile):
    maps = []
    source = 'maps/' + str(nameFile)
    with open(source, 'r') as file:
        for i in range(0, 100):
            maps.append(file.readline().replace('\n', '').split(',')[0:-1])
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == '1':
                down = Down(down_image, pos)
                down_group.add(down)
            elif maps[i][j] == '2':
                bush = bush(bush_image, pos)
                bush_group.add(bush)
            elif maps[i][j] == '3':
                bush = Bush_tower(bush_tower_image, pos)
                bush_tower_group.add(bush)
            elif maps[i][j] == '4':
                grass = Grass(grass_image, pos)
                grass_group.add(grass)
            elif maps[i][j] == '5':
                right = Right(right_image, pos)
                right_group.add(right)
            elif maps[i][j] == '6':
                up = Up(up_image, pos)
                up_group.add(up)
def game_lvl():
    sc.fill('gray')
    down_group.draw(sc)
    bush_group.draw(sc)
    bush_tower_group.draw(sc)
_group.draw(sc)
restart()
drawMaps('maps1.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
