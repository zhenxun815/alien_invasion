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

        # set ship appearance location
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship location according to the moving flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        """draw spaceship"""
        self.screen.blit(self.image, self.rect)
