#!/usr/bin/env python
# -*- coding=UTF-8 -*-
"""
    众所周知，牛妹非常喜欢吃蛋糕。
    第一天牛妹吃掉蛋糕总数三分之一（向下取整）多一个，第二天又将剩下的蛋糕吃掉三分之一（向下取整）多一个，
    以后每天吃掉前一天剩下的三分之一（向下取整）多一个，到第n天准备吃的时候只剩下一个蛋糕。
    牛妹想知道第一天开始吃的时候蛋糕一共有多少呢？
"""

# @param n int整型 只剩下一只蛋糕的时候是在第n天发生的．
# @return int整型
#
import math


class Solution:

    def eatCake(self, total, n):
        print n, total
        eatNum = math.floor(float(total)/3) + 1
        total -= eatNum
        if n == 1:
            return total
        else:
            self.eatCake(total, n - 1)

    def cakeNumber(self, n):
        # write code here
        total = 1
        if n == 1:
            return total
        else:
            for i in range(1, n):
                print  i, total
                total = (total + 1) * 3 / 2

            return total

if __name__ == '__main__':
     s = Solution()
     # s.eatCake( 16, 5)
     s.cakeNumber(6)