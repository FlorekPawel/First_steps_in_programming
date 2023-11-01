import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
       
        #inicjalizaj i położenie pocz
        self.screen = screen

        #wczytanie obrazka
        self.image = pygame.image.load('images/ship.bmp')
        #zrobienie z niego prostokąta
        self.rect = self.image.get_rect()
        #wczytanie ustawień ekranu
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        #pojawienie się statku na dole ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #położenie jako liczba niecałkowita
        self.center = float(self.rect.centerx)

        #poruszanie
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        #wyświetlanie rakiety w aktualnym położeniu
        self.screen.blit(self.image, self.rect)

    def moving(self):
        #zmiana położenia statku, statek nie może wylecieć za ekran
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #uaktualnienie pozycji do wyświetlania
        self.rect.centerx = self.center

    def center_ship(self):
        #wyśrodkowanie statku
        self.center = self.screen_rect.centerx