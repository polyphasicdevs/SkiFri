import pygame

# Initialize pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)

# Load images
skier_center_image = pygame.image.load("skier.png")
skier_left_image = pygame.image.load("skier_left.png")
skier_right_image = pygame.image.load("skier_right.png")
skier_fast_image = pygame.image.load("skier_fast.png")
skier_jump_image = pygame.image.load("skier_jump.png")
skier_crash_image = pygame.image.load("skier_crash.png")

tree_image = pygame.image.load("tree.png")
rock_image = pygame.image.load("rock.png")
yeti_image = pygame.image.load("yeti.png")

# Base speed of the skier
base_speed = 3

