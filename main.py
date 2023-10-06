import pygame
import random
from settings import *
from player import Skier
from obstacles import Obstacle
from yeti import Yeti
from game_over import game_over_screen

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SkiFree Recreation")

# Initialize skier, obstacles, and yeti
skier = Skier()
obstacles = []
yeti = Yeti()

OBSTACLE_FREQUENCY = 100  # The smaller, the more frequent

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not skier.jumping:
                skier.jump()

    keys = pygame.key.get_pressed()
    skier.move(keys)

    # Generate and move obstacles
    if random.randint(1, OBSTACLE_FREQUENCY) == 1:
        obstacles.append(Obstacle())

    for obstacle in obstacles:
        obstacle.move(skier.speed)
        if obstacle.rect.y + obstacle.rect.height < 0:  # If obstacle is off the screen
            obstacles.remove(obstacle)

    # Collision detection
    for obstacle in obstacles:
        if skier.rect.colliderect(obstacle.rect):
            if obstacle.type == "rock" and skier.jumping:
                continue  # Skip collision if jumping over a rock
            skier.collide()  # Use the collide method to change sprite
            game_over_screen(screen)  # Display the game over screen
            running = False

    # Yeti chase
    if pygame.time.get_ticks() > 600 and not yeti.active:
        yeti.active = True

    if yeti.active:
        yeti.chase()
        if yeti.rect.colliderect(skier.rect):
            skier.collide()  # Use the collide method to change sprite
            game_over_screen(screen)  # Display the game over screen
            running = False

    # Drawing
    screen.fill(WHITE)
    screen.blit(skier.image, skier.rect.topleft)
    for obstacle in obstacles:
        screen.blit(obstacle.image, obstacle.rect.topleft)
    if yeti.active:
        screen.blit(yeti.image, yeti.rect.topleft)

    pygame.display.flip()

pygame.quit()
