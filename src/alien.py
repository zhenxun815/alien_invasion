#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: alien
# @Project: alien_invasion
# @Author: yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/6/4 下午8:06

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class represent enemy"""

    def __init__(self, ai_settings, screen):
        """ init  alien obj and set appearance location"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # load alien img and set its rect attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # set appearance location near left-top conner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """ if aliens move to screen edge, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """draw alien"""
        self.screen.blit(self.image, self.rect)
