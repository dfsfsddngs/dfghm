from pygame import *

win_width = 700
win_height = 500
'''background = (51, 195, 214)'''
display.set_caption("Пинг-Понг")
fon = "contrast-test.png"
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load( "5162027.jpg"), (win_width, win_height))
img_hero = "racket.png"
img_ball = "ball.png"

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def resel(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5 and self.rect.y < 490:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y > 5 and self.rect.y < 490:
           self.rect.x += self.speed

player1 = Player(img_hero,50,50,20,500,5)


game = True

while game :
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    player1.resel()
    player1.update()
    display.update()
    time.delay(30)