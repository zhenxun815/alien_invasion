#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: alien_invasion
# @Project: alien_invasion
# @Author: yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/6/2 上午10:29

import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    """main function"""
    # init the game and create a screen obj
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a space ship
    ship = Ship(ai_settings, screen)
    # create a group to store bullets
    bullets = Group()
    # create aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # start the main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
