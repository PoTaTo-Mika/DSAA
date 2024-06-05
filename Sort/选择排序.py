#-*- coding:UTF-8 -*-
import random
class select_sort():
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
list_test = []
for l in range(20):
    list_test.append(random.randint(1,100))
print(list_test)
sort = select_sort(list_test)
print(sort.select_sort())
                    
                
                