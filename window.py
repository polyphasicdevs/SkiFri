import pygame
import random

# Initialize pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SkiFree Recreation")

# Load images
skier_center_image = pygame.image.load("skier.png")
skier_left_image = pygame.image.load("skier_left.png")
skier_right_image = pygame.image.load("skier_right.png")
skier_fast_image = pygame.image.load("skier_fast.png")
skier_jump_image = pygame.image.load("skier_jump.png")
skier_crash_image = pygame.image.load("skier_crash.png")
current_skier_image = skier_center_image

tree_image = pygame.image.load("tree.png")
rock_image = pygame.image.load("rock.png")
yeti_image = pygame.image.load("yeti.png")

# Skier properties
skier_rect = skier_center_image.get_rect()
skier_rect.center = (WIDTH // 2, 50)  # Position the skier towards the top
base_speed = 3  # Base speed of the skier
speed = base_speed

# Jump properties
jumping = False
jump_duration = 1000  # 1 second
jump_start_time = None

# Obstacles
obstacles = []
OBSTACLE_FREQUENCY = 100  # The smaller, the more frequent

def generate_obstacle():
    obstacle_type = random.choice(["tree", "rock"])
    if obstacle_type == "tree":
        image = tree_image
    else:
        image = rock_image
    rect = image.get_rect()
    rect.x = random.randint(0, WIDTH - rect.width)
    rect.y = HEIGHT  # Start at the bottom
    return {"type": obstacle_type, "image": image, "rect": rect}

# Yeti properties
yeti_rect = yeti_image.get_rect()
yeti_rect.x = random.randint(0, WIDTH - yeti_rect.width)
yeti_rect.y = HEIGHT  # Start at the bottom
yeti_speed = 3
yeti_active = False

def game_over_screen():
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over', True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    
    ok_font = pygame.font.Font(None, 50)
    ok_text = ok_font.render('Press OK to exit', True, (0, 0, 255))
    ok_rect = ok_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    
    screen.blit(text, text_rect)
    screen.blit(ok_text, ok_rect)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    waiting = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                jump_start_time = pygame.time.get_ticks()
                current_skier_image = skier_jump_image

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and skier_rect.left > 0:
        skier_rect.x -= speed
        current_skier_image = skier_left_image
    elif keys[pygame.K_RIGHT] and skier_rect.right < WIDTH:
        skier_rect.x += speed
        current_skier_image = skier_right_image
    elif keys[pygame.K_DOWN]:
        speed = base_speed * 1.3
        current_skier_image = skier_fast_image
    else:
        speed = base_speed
        current_skier_image = skier_center_image

    if jumping:
        if pygame.time.get_ticks() - jump_start_time > jump_duration:
            jumping = False
            current_skier_image = skier_center_image

    # Generate and move obstacles
    if random.randint(1, OBSTACLE_FREQUENCY) == 1:
        obstacles.append(generate_obstacle())

    for obstacle in obstacles:
        obstacle["rect"].y -= speed  # Move obstacles upwards
        if obstacle["rect"].y + obstacle["rect"].height < 0:  # If obstacle is off the screen
            obstacles.remove(obstacle)

    # Collision detection
    for obstacle in obstacles:
        if skier_rect.colliderect(obstacle["rect"]):
            if obstacle["type"] == "rock" and jumping:
                continue  # Skip collision if jumping over a rock
            current_skier_image = skier_crash_image
            game_over_screen()
            pygame.quit()
            exit()

    # Yeti chase
    if pygame.time.get_ticks() > 10000 and not yeti_active:
        yeti_active = True

    if yeti_active:
        yeti_rect.y -= yeti_speed  # Move Yeti upwards
        if yeti_rect.colliderect(skier_rect):
            current_skier_image = skier_crash_image
            game_over_screen()
            pygame.quit()
            exit()

    # Drawing
    screen.fill(WHITE)
    screen.blit(current_skier_image, skier_rect.topleft)
    for obstacle in obstacles:
        screen.blit(obstacle["image"], obstacle["rect"].topleft)
    if yeti_active:
        screen.blit(yeti_image, yeti_rect.topleft)

    pygame.display.flip()

pygame.quit()
