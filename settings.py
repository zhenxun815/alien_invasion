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
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed_factor = 1.5
