#создай игру "Лабиринт"!
from pygame import *

#Объявляем классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = None
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite) :
    def updatel(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 50:
            self.rect.y += self.speed
    def updater(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 50:
            self.rect.y += self.speed
    def updateb(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_KP8] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_KP2] and self.rect.y < win_height - 50:
            self.rect.y += self.speed
        if keys_pressed[K_KP4] and self.rect.x < 5000:
            self.rect.x -= self.speed
        if keys_pressed[K_KP6] and self.rect.x > -5000:
            self.rect.x += self.speed

#создай окно игры
win_width = 1280
win_height = 800
window = display.set_mode((win_width, win_height))
window.fill((0,0,255))
display.set_caption('ДичеТенис')
#background = transform.scale(image.load("grass.jpg"), (win_width, win_height))

#создай 2 спрайта и размести их на сцене
player1 = Player('Player1.png', 25, (win_height / 2), 225, 225, 4)
player2 = Player('Player2.png', win_width - 250, (win_height / 2), 225, 225, 4)

#мяч
ball = GameSprite('ball.png', 600, (win_height / 2), 50, 50, 4)

#Задать FPS
clock = time.Clock()
FPS = 120

font.init()
font1 = font.SysFont('Arial', 70)

#Счёт
score = 0
score = font1.render(str(score), True, (250, 255, 0))

#Выигрыш
#Win1 = font1.render('1 Игрок выигрывает')
#Win2 = font1.render('2 Игрок выигрывает')

#GoalPlayer1 = font1.render('1 Игрок забивает ГОЛ', True, (255, 0 , 0))
#GoalPlayer2 = font1.render('2 Игрок забивает ГОЛ', True, (0, 0 , 255))

#обработай событие «клик по кнопке "Закрыть окно"»

speed_x = 3
speed_y = 3

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player1.rect.x = 25
                player1.rect.y = (win_height / 2)
                player2.rect.x = win_width - 250
                player2.rect.y =  (win_height / 2)
                ball.rect.x = 600
                ball.rect.y = (win_height / 2)
                finish = False

    window.fill((0,0,255))

    if not finish :
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y >= 750:
            speed_y *= -1
    
        if ball.rect.y <= 0:
            speed_y *= -1

        if sprite.collide_rect(player2, ball):
            speed_x *= -1

        if sprite.collide_rect(player1, ball):
            speed_x *= -1

        #if ball.rect.x = 1280:

    
    player1.reset()
    player2.reset()
    ball.reset()

    player1.updatel()
    player2.updater()
    
    display.update()
    clock.tick(FPS)