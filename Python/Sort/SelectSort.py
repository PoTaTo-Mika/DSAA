#-*- coding:UTF-8 -*-
import random
class SelectSort():
    def __init__(self,alist):
        self.alist = alist
    def select_sort(self):
        num = 0
        label = 0
        for i in range(len(self.alist)):
            for k in range(i,len(self.alist)):
                if self.alist[i] < self.alist[k]:
                     self.alist[i], self.alist[k] = self.alist[k], self.alist[i]
        return self.alist

                