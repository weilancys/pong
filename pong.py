import pygame

# https://realpython.com/pygame-a-primer/#collision-detection
# https://www.youtube.com/watch?v=tS8F7_X2qB0
# https://gamedev.stackexchange.com/questions/4253/in-pong-how-do-you-calculate-the-balls-direction-when-it-bounces-off-the-paddl

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
class PaddleConfig:
    def __init__(self, up_key, down_key, speed=8, width=10, height=120, initial_x=30, initial_y=10, color=WHITE):
        self.color = color
        self.width = width
        self.height = height
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.speed = speed
        self.up_key = up_key
        self.down_key = down_key

class Paddle(pygame.sprite.Sprite):
    def __init__(self, config: PaddleConfig):
        super().__init__()
        self.config = config
        self.surface = pygame.surface.Surface((config.width, config.height))
        self.surface.fill(config.color)
        self.rect = self.surface.get_rect()
        self.rect.x = config.initial_x
        self.rect.y = config.initial_y

    def move(self):
        key_pressed = pygame.key.get_pressed()
        if self.rect.y < 0:
            self.rect.y = 0
            return
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            return
        if key_pressed[self.config.up_key]:
            self.rect.move_ip(0, self.config.speed * -1)
        elif key_pressed[self.config.down_key]:
            self.rect.move_ip(0, self.config.speed)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 20
        self.radius = self.width / 2
        self.SPEED = 8
        self.speed_x = self.SPEED
        self.speed_y = self.SPEED
        self.surface = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
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
        
config_left = PaddleConfig(pygame.K_w, pygame.K_s, initial_x=30, initial_y=SCREEN_HEIGHT // 2 - 60)
paddle_left = Paddle(config=config_left)
config_right = PaddleConfig(pygame.K_UP, pygame.K_DOWN, initial_x=SCREEN_WIDTH - 30 - 10, initial_y=SCREEN_HEIGHT // 2 - 60)
paddle_right = Paddle(config=config_right)
ball = Ball()
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle_left)
all_sprites.add(paddle_right)
all_sprites.add(ball)
paddles = pygame.sprite.Group()
paddles.add(paddle_left)
paddles.add(paddle_right)

running = True

# main loop
while running:
    # fill screen with BLACK
    screen.fill(BLACK)

    # user input
    paddle_left.move()
    paddle_right.move()
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