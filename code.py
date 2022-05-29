from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_h - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_h - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
window.fill(back)

game = True
finish = False
clock = time.Clock()
fps = 50

rocket1 = Player('racket.png', 30, 200, 4, 20, 100)
rocket2 = Player('racket.png', 520, 200, 4, 20, 100)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 30, 30)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOST!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOST!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
        if ball.rect.y > win_h - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        if ball.rect.x > win_w - 50:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True         
        
        rocket1.reset()
        rocket2.reset()
        ball.reset()
    display.update()
    clock.tick(fps)