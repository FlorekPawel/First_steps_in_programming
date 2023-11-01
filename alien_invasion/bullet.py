import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        
        #utworzenie pocisku w pkt (0,0) i zdefiniowaniu położenia na górnym środku statku 
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #położenie pocisku jako liczba niecałkowita
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #uaktualnienie położenia pocisku
        self.y -= self.speed_factor
        #uaktualnienie położenia prostokąta pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        #uaktualnienie na ekranie
        pygame.draw.rect(self.screen, self.color, self.rect)

    