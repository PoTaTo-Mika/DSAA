#-*- coding:UTF-8 -*-
import random

class seer_sort():
    
    def __init__(self,alist):
        self.alist = alist

    def seer_sort(self):
        n = len(self.alist)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.alist[i]
                j = i
                while j >= gap and self.alist[j - gap] > temp:
                    self.alist[j] = self.alist[j - gap]
                    j -= gap
                self.alist[j] = temp
            gap //= 2 
        return self.alist
