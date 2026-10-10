#create a Maze game!
from pygame import *

class Gamesprite():
    def __init__(self, p_image, x, y, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def control_player2(self):
        presskeys = key.get_pressed()
        if presskeys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if presskeys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed


    def control_player1(self):
        presskeys = key.get_pressed()
        if presskeys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if presskeys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed
        
class Ball(Gamesprite):
    pass



ww = 700
wh = 500
window = display.set_mode((ww, wh))
window.fill((102,255,255))
display.set_caption('Ping Pong')

#bg = transform.scale(image.load('background.jpg'), (ww, wh))
ball= Ball('ball.png', 220, 220, 10, 50, 50)
player1= Player('paddle.png', 40,150, 10, 30, 100) 
player2 = Player('paddle.png', 630,150, 10, 30, 100) 



game = True
clock = time.Clock()
fps = 60
finish = False



font.init()
font = font.Font(None, 70)
win = font.render('You won!', True, (255, 215, 0))
lose = font.render('You lost!', True, (255, 215, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((102,255,255))
        player1.reset()
        player2.reset()
        ball.reset()
        player2.control_player2()
        player1.control_player1()

    display.update()
    clock.tick(fps)

