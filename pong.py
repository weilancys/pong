import pygame

# https://realpython.com/pygame-a-primer/#collision-detection
# https://www.youtube.com/watch?v=tS8F7_X2qB0

# init
SCREEN_WIDTH, SCREEN_HEIGHT = 1027, 768
pygame.init()
pygame.display.set_caption("pong")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (123, 123, 123)

# sprites
class PaddleLeft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 120
        self.surface = pygame.surface.Surface((self.width, self.height))
        self.surface.fill(WHITE)
        self.rect = self.surface.get_rect()
        self.rect.x = 20
        self.rect.y = SCREEN_HEIGHT / 2 - self.height / 2
        self.speed = 8

    def move(self, key_pressed):
        if self.rect.y < 0:
            self.rect.y = 0
            return
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            return
        if key_pressed[pygame.K_w]:
            print("w pressed")
            self.rect.move_ip(0, self.speed * -1)
        elif key_pressed[pygame.K_s]:
            print("s pressed")
            self.rect.move_ip(0, self.speed)

class PaddleRight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 120
        self.surface = pygame.surface.Surface((self.width, self.height))
        self.surface.fill(WHITE)
        self.rect = self.surface.get_rect()
        self.rect.x = SCREEN_WIDTH - self.width - 20
        self.rect.y = SCREEN_HEIGHT / 2 - self.height / 2
        self.speed = 8

    def move(self, key_pressed):
        if self.rect.y < 0:
            self.rect.y = 0
            return
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            return
        if key_pressed[pygame.K_UP]:
            print("up pressed")
            self.rect.move_ip(0, self.speed * -1)
        elif key_pressed[pygame.K_DOWN]:
            print("down pressed")
            self.rect.move_ip(0, self.speed)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 20
        self.radius = self.width / 2
        self.SPEED = 8
        self.speed_x = self.SPEED
        self.speed_y = self.SPEED
        self.surface = pygame.surface.Surface((self.width, self.height))
        # self.surface.fill(GRAY)
        self.rect = self.surface.get_rect()
        pygame.draw.circle(self.surface, WHITE, self.rect.center, self.radius)

    def move(self, paddles: pygame.sprite.Group):
        if self.rect.x < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x = self.speed_x * -1
        if self.rect.y < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y = self.speed_y * -1
        if pygame.sprite.spritecollideany(self, paddles):
            self.speed_x = self.speed_x * -1
        self.rect.move_ip(self.speed_x, self.speed_y)
        

paddle_left = PaddleLeft()
paddle_right = PaddleRight()
ball = Ball()
paddles = pygame.sprite.Group()
paddles.add(paddle_left)
paddles.add(paddle_right)

running = True

# main loop
while running:
    # fill screen with BLACK
    screen.fill(BLACK)

    # user input
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_s]:
        print("s pressed")
    paddle_left.move(key_pressed)
    paddle_right.move(key_pressed)
    ball.move(paddles)

    # events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    # draw
    screen.blit(paddle_left.surface, paddle_left.rect)
    screen.blit(paddle_right.surface, paddle_right.rect)
    screen.blit(ball.surface, ball.rect)

    # update the screen
    pygame.display.update()

    # 60fps
    clock.tick(FPS)

pygame.quit()