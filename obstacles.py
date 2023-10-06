import pygame
import random
from settings import *

class Obstacle:
    def __init__(self):
        self.type = random.choice(["tree", "rock"])
        self.image = tree_image if self.type == "tree" else rock_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = HEIGHT

    def move(self, speed):
        self.rect.y -= speed

