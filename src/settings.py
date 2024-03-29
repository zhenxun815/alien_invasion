#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: settings
# @Project: alien_invasion
# @Author: yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/6/2 下午5:54


class Settings:
    """ store all settings"""

    def __init__(self):
        """init game settings"""
        # display setting
        self.screen_width = 1400
        self.screen_height = 1400
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 right, -1 left
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 20
