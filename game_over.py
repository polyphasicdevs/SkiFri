import pygame
from settings import *

def game_over_screen(screen):  # Add screen as an argument
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over', True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    
    ok_font = pygame.font.Font(None, 50)
    ok_text = ok_font.render('Press Enter to exit', True, (0, 0, 255))
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
                if event.key == pygame.K_RETURN:
                    waiting = False

