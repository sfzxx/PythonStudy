import pygame
import sys
import random

# 全局定义
SCREEN_X = 600
SCREEN_Y = 600


# 蛇类
# 点以25为单位
class Snake(object):
    # 初始化各种需要的属性（开始时默认向右、身体块×5）
    def_init_(self):
        self.dirction = pygame.K.RIFHT
        self.body = []
        for x in range(5):
            self.addnode()

    # 无论何时，都在前端增加蛇块
    def addnode