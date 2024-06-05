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
    
list_test = []
for l in range(20):
    list_test.append(random.randint(1,100))
print(list_test)
seer = seer_sort(list_test)
print(seer.seer_sort())