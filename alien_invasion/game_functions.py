import sys

import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, stats, aliens, ship, ai_settings, screen, bullets):
    #reagowanie na wściśniecie klawisza
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, stats, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_g:
            if not stats.game_active:
                stats.reset_stats()
                stats.game_active = True
                aliens.empty()
                bullets.empty()
                create_fleet(ai_settings, screen, ship, aliens)
                ship.center_ship()
                ai_settings.initialize_dinamic_settings()
                pygame.mouse.set_visible(False)
                

def check_keyup_events(event, ship):
    #reagowanie na puszczenie klawisza
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def fire_bullet(ai_settings, stats, screen, ship, bullets):
    if stats.game_active:
        if len(bullets) < ai_settings.max_bullets:
            #utworzenie nowego pocisku
            new_bullet = Bullet(ai_settings, screen, ship)
            #dodanie go do grupy
            bullets.add(new_bullet)

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    #reakcja na klaw/mysz

    for event in pygame.event.get():
        #zamknięcie oknia -> koniec gry
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, stats, aliens, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    #rozp gry po kliknieciu przycisku
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset gry i rozp
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        ai_settings.initialize_dinamic_settings()
        sb.prep_score()
        sb.prep_best_score()
        sb.prep_lvl()
        sb.prep_ship()
        #ukrycie kursora
        pygame.mouse.set_visible(False)
        

def get_number_aliens(ai_settings, alien_width):
    #ustalenie l. obcych
    #odległość miedzy obc = ich szerokość
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    #ustalenie l. rzędów obcych
    available_space = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #utworzenie obcego i dodanie do rzędu
        alien = Alien(ai_settings, screen)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 *alien.rect.height * row_number
        aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    #tworzenie floty
    
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    #utworzenie floty obcych
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    #odświeżenie okranu
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    #wyświetlanie pocisków
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #przycisk start
    if not stats.game_active:
        play_button.draw_button()
    #pokazywanie zmienionego ekranu
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #uaktulanienie połozenie i usuniecie tych za ekranem
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    
    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, bullets, aliens)
    
def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, bullets, aliens):    
    #sprawdzenie trafienia pocisku
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

            check_best_score(stats, sb)

    #respienie ponowne floty
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.game_lvl += 1
        sb.prep_lvl()
        

def check_fleet_edges(ai_settings, aliens):
    #sprawdzenie czy flota na krawędzi
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    #zmiana kierunku i opadnięcie floty
    ai_settings.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #kolizja ze statkiem
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    #dotarcie na dół
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)
        
def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    #reakcja na uderzeie w statek
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ship()
        #reset
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    #pauza
    sleep(0.5)

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def check_best_score(stats, sb):
    if stats.best_score < stats.score:
        stats.best_score = stats.score
        sb.prep_best_score()
        