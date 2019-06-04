#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: bullet
# @Project: alien_invasion
# @Author: yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/6/3 下午11:33

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class to manage bullets"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet obj at ship location"""
        super().__init__()
        self.screen = screen

        # create a rect at (0,0) point which represents a bullet obj, the set it to right location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move bullet up"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
