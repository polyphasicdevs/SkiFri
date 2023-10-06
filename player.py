import pygame
from settings import *

class Skier:
    def __init__(self):
        self.image = skier_center_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 50)
        self.speed = base_speed
        self.jumping = False
        self.jump_duration = 1000
        self.jump_start_time = None

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.image = skier_left_image
        elif keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.image = skier_right_image
        elif keys[pygame.K_DOWN]:
            self.speed = base_speed * 1.3
            if self.rect.bottom < HEIGHT:
                self.rect.y += int(self.speed * 0.3)
            self.image = skier_fast_image
        else:
            self.speed = base_speed
            self.image = skier_center_image

    def jump(self):
        self.jumping = True
        self.jump_start_time = pygame.time.get_ticks()
        self.image = skier_jump_image  # Change sprite to jump image
    def collide(self):
        self.image = skier_crash_image  # Change sprite to crash image

    def update(self):
        if self.jumping:
            if pygame.time.get_ticks() - self.jump_start_time > self.jump_duration:
                self.jumping = False
                self.image = skier_center_image  # Revert back to the center image after jump

