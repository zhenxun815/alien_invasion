#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: alien_invasion
# @Project: alien_invasion
# @Author: yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/6/2 上午10:29

import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    """game enter function"""
    # init the game and create a screen obj
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a space ship
    ship = Ship(ai_settings, screen)
    # create a group to store bullets
    bullets = Group()
    # start the main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        delete_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)


def delete_bullets(bullets):
    """delete out screen bullets"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # print(len(bullets))


run_game()
