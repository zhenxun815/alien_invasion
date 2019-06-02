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


def check_events():
    """listen the keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
