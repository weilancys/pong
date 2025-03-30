import pygame

pygame.init()

FPS = 30
clock = pygame.time.Clock()

pygame.display.set_caption("test")
screen = pygame.display.set_mode((300, 300))
running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            print(e.key)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_a]: print("A pressed")
    # if keys[pygame.K_s]: print("S pressed")
    # if keys[pygame.K_d]: print("D pressed")
    # if keys[pygame.K_f]: print("F pressed")
    # if keys[pygame.K_UP]: print("Up pressed")
    # if keys[pygame.K_ESCAPE]: print("Escape pressed")

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()