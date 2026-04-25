from pygame import *
from random import randint
from time import time as timer
mixer.init()

win_width = 700
win_height = 500
display.set_caption("Пинг-Понг")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('51, 195, 214'), (win_width, win_height))

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5 and self.rect.y < 490:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y > 5 and self.rect.y < 490:
           self.rect.x += self.speed
   def fire(self):
       bullet = Bullet(img_bullet, self.rect.x+32.5, self.rect.top, 15, 20, -15)
       bullets.add(bullet)

game = True

while game :
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
