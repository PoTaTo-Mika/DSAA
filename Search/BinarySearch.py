import random as rd
from QuickSort import QuickSort

class BinarySearch():
    
    def __init__(self,alist,num):
        self.alist = QuickSort(alist).sort()
        self.num = num
    
    def BinarySearch(self):
        left,right = 0,len(self.alist)
        while left <= right:
            mid = (left + right) // 2
            if self.num > self.alist[mid]:
                left = mid
            else:
                if self.num < self.alist[mid]:
                    right = mid
                else:
                    if self.num == self.alist[mid]:
                        return mid+1
                    else:
                        return -1
            