#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: ship
# @Project: alien_invasion
# @Author: yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/6/2 下午6:28

import pygame


class Ship:

    def __init__(self, screen):
        """init the ship ,set its appearance location"""
        self.screen = screen
        # load ship img
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw spaceship"""
        self.screen.blit(self.image, self.rect)
