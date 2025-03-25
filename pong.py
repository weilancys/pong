import pygame

# https://realpython.com/pygame-a-primer/#collision-detection
# https://www.youtube.com/watch?v=tS8F7_X2qB0

# init
WIDTH, HEIGHT = 1000, 600
pygame.init()
pygame.display.set_caption("pong")
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ball
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_radius = 10
ball_speed = 6

# paddle
paddle_width = 10
paddle_height = 100
PADDLE_SPEED = 9
paddle_speed = 0
paddle_left_x = 30
paddle_left_y = 40

running = True

# main loop
while running:
    # fill screen with BLACK
    window.fill(BLACK)

    # events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                paddle_speed = PADDLE_SPEED * -1
            elif e.key == pygame.K_DOWN:
                paddle_speed = PADDLE_SPEED
        if e.type == pygame.KEYUP:
            paddle_speed = 0

    # paddle movement
    paddle_left_y += paddle_speed
    if paddle_left_y + paddle_height >= HEIGHT:
        paddle_left_y = HEIGHT - paddle_height
    if paddle_left_y <= 0:
        paddle_left_y = 0
    
    # ball movement
    if ball_x + ball_radius * 2 >= WIDTH or ball_x <= 0:
        ball_speed = ball_speed * -1
    if ball_x - ball_radius <= paddle_left_x + paddle_width and ball_y + ball_radius <= paddle_left_y + paddle_height and ball_y - ball_radius >= paddle_left_y:
        ball_speed = ball_speed * -1
    ball_x += ball_speed
    
    # draw
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(window, RED, pygame.Rect(paddle_left_x, paddle_left_y, paddle_width, paddle_height))

    # update the screen
    pygame.display.update()

    # 60fps
    clock.tick(FPS)

pygame.quit()