class Settings():
    #ustawienia
    def __init__(self):
        #ekran
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #statek
        self.ship_limit = 3
        #pocisk
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.max_bullets = 8
        #obcy
        self.fleet_drop_speed = 9
        self.fleet_direction = 1
        self.alien_points = 50
        #poziomy trudności
        self.speedup_factor = 1.3
        self.score_scale = 1.5

        self.initialize_dinamic_settings()

    def initialize_dinamic_settings(self):
        self.alien_speed_factor = 0.2
        self.ship_speed_factor = 0.6
        self.bullet_speed_factor = 1.2

    def increase_speed(self):    
        #zmiana poziomu tr
        self.alien_speed_factor *= self.speedup_factor
        #self.ship_speed_factor *= self.speedup_factor
        #self.bullet_speed_factor *= self.speedup_factor
        self.alien_points = int(self.score_scale * self.alien_points)