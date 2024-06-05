#-*- coding:UTF-8 -*-
import random

class bubble_sort():
    def __init__(self,alist):
        self.alist = alist
    def sort(self):
        for i in range(len(self.alist)-1):
            for k in range(len(self.alist)-1-i):
                if self.alist[k] < self.alist[k+1]:
                    self.alist[k], self.alist[k+1] = self.alist[k+1], self.alist[k]
        return self.alist
    
