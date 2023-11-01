import pygame.font 
from ship import Ship
from pygame.sprite import Group

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_best_score()
        self.prep_lvl()
        self.prep_ship()
    
    def prep_score(self):
        #generowanie obrazu
        rounded_score = int(round(self.stats.score, -1))
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_best_score(self):
        best_score = int(round(self.stats.best_score, -1))
        best_score_str = '{:,}'.format(best_score)
        self.best_score_image = self.font.render(best_score_str, True, self.text_color, self.ai_settings.bg_color)

        self.best_score_rect = self.best_score_image.get_rect()
        self.best_score_rect.right = self.screen_rect.right - 20
        self.best_score_rect.top = 60

    def prep_lvl(self):
        self.lvl_image = self.font.render('lvl ' + str(self.stats.game_lvl), True, self.text_color, self.ai_settings.bg_color)

        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.centerx = self.screen_rect.centerx
        self.lvl_rect.top = 20
    
    def prep_ship(self):
        self.ships = Group()
        for ship_number in range (self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.best_score_image, self.best_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)

    