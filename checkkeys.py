import pygame

pygame.init()
FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Keyboard Test")
running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            print(f"Key pressed - Scancode: {e.scancode}, Keycode: {e.key}, Unicode: {e.unicode}")
    
    screen.fill((0, 0, 0))
    if pygame.key.get_focused():
        pygame.draw.circle(screen, (0, 255, 0), (20, 20), 10)
    else:
        pygame.draw.circle(screen, (255, 0, 0), (20, 20), 10)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[ord('a')]: print("A pressed")
    if keys[pygame.K_b]: print("B pressed")  # Test another key
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()