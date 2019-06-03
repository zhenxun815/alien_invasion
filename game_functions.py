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


def check_key_down_events(event, ship):
    """listen key down events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_key_up_events(event, ship):
    """listen key up events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """listen the keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """redraw surfaces and update the display"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
