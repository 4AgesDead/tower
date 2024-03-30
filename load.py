from script import load_image
from pygame import image

enemy_image = image.load('image/enemy/right.png').convert_alpha()
down_image = image.load('image/tile map/bottom.png').convert_alpha()
bush_image = image.load('image/tile map/bush_tile 1.png').convert_alpha()
bush_tower_image = image.load('image/tile map/bush_tile_tower.png').convert_alpha()
left_image = image.load('image/tile map/left.png').convert_alpha()
right_image = image.load('image/tile map/right.png').convert_alpha()
up_image = image.load('image/tile map/top.png').convert_alpha()
tower_off_image = image.load('image/tower 1/1_of.png').convert_alpha()
tower_on_image = image.load('image/tower 1/1_on.png').convert_alpha()
tower_image=load_image('image/tower 1/tower')
bullet_image = image.load('image/tower 1/bullet 1.png').convert_alpha()
tower2_image = image.load('image/tower 1_1/bullet 2.png').convert_alpha()
tower_image=load_image('image/tower 1_1/tower')
bar_image = image.load('image/panel.jpg').convert_alpha()
upgrade_image = image.load('image/upgrade.png').convert_alpha()
grass_image = image.load('image/tile map/grass_tile_1.png').convert_alpha()
