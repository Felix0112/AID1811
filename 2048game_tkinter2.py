#！／usr/bin/env python3
# -*- coding:utf-8 -*-

# Author : 魏明择
#　Date : 2017

#参考网址: http://2048game.com


import random
import math


__mataclass__ = type #使用新式类


# 此类为地图模块封装的类
class map2048():

    #重新设置游戏数据
    def reset(self):
        self.__row = 4 #行数
        self.__col = 4 #列数
        self.data = [
            [0 for x in range(self.__col)]
            for y in range(self.__row)
        ]
        #self.data = [[x+4*y for x in range(self.__col)]
        #               for y in range(self.__row)]
        # self.data = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.fill2()
        self.fill2()

    def __init__(self):
        self.reset()
    
    #获取没有数字的位置的个数
    def get_space_count(self):
        """
        获取没有数字的方格的数据
        """
        count = 0
        for r in self.data:
            count += r.count(0)
        return count 
    #获得游戏的得数
    def　get_score(self):
        s = 0
        for r in self.data:
            for c in r:
                s += 0 if c < 4