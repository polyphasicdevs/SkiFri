import pygame
import random
from settings import *

class Yeti:
    def __init__(self):
        self.image = yeti_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = HEIGHT
        self.speed = 3
        self.active = False

    def chase(self):
        self.rect.y -= self.speed

