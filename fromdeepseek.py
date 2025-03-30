import pygame
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (123, 123, 123)
FPS = 60

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 10
        self.height = 120
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 8

    def update(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key]:
            self.rect.y -= self.speed
        if keys[down_key]:
            self.rect.y += self.speed
        
        # Keep paddle on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 10
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.reset()
        self.speed = 8
        
    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.dx = self.speed * (1 if pygame.time.get_ticks() % 2 == 0 else -1)
        self.dy = self.speed * (1 if pygame.time.get_ticks() % 3 == 0 else -1)
        
    def update(self, paddles):
        # Move the ball
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        # Wall collisions (top and bottom)
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy *= -1
            
        # Paddle collisions
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                # Reverse direction and add slight angle change based on where ball hits paddle
                self.dx *= -1
                offset = (self.rect.centery - paddle.rect.centery) / (paddle.height / 2)
                self.dy = offset * self.speed
                
        # Score (left and right walls)
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.reset()

# Create sprites
paddle_left = Paddle(20, SCREEN_HEIGHT // 2 - 60)
paddle_right = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - 60)
ball = Ball()
all_sprites = pygame.sprite.Group(paddle_left, paddle_right, ball)
paddles = pygame.sprite.Group(paddle_left, paddle_right)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Update
    paddle_left.update(pygame.K_w, pygame.K_s)
    paddle_right.update(pygame.K_UP, pygame.K_DOWN)
    ball.update(paddles)
    
    # Draw
    screen.fill(BLACK)
    pygame.draw.line(screen, GRAY, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 1)
    all_sprites.draw(screen)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()