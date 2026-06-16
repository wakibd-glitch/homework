import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Add Sprites")

clock = pygame.time.Clock()

# Sprite rectangles
player = pygame.Rect(100, 100, 80, 60)
sprite2 = pygame.Rect(500, 250, 120, 80)

speed = 5
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 120, 255), player)
    pygame.draw.rect(screen, (255, 80, 80), sprite2)

    pygame.display.update()
    clock.tick(60)

pygame.quit()