import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    #inicjalizacja i tworzenie ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    
    #stworzenie statku oraz gr pocisków i obcych
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, 'Gra')

    gf.create_fleet(ai_settings, screen, ship, aliens)
    

    
    #pętla główna gry
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:    
            ship.moving()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()