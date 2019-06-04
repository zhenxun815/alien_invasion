#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: game_functions
# @Project: alien_invasion
# @Author: yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/6/2 下午8:18

import sys
import pygame
from src.bullet import Bullet


def check_key_down_events(event, ai_settings, screen, ship, bullets):
    """listen key down events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """add one new bullet and add to group"""
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_key_up_events(event, ship):
    """listen key up events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_setttings, screen, ship, bullets):
    """listen the keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_setttings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """redraw surfaces and update the display"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    """draw ,move and remove bullets"""
    bullets.update()
    # delete out screen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # print(len(bullets))