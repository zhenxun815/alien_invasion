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


def run_game():
    # init the game and create a screen obj
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a space ship
    ship = Ship(ai_settings, screen)
    # start the main loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
