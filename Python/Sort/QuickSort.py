import random as rd

class QuickSort():
    
    def __init__(self,alist):
        self.alist = alist
        
    def Partition(self,left,right):
        benchmark = self.alist[right]
        i = left - 1
        for j in range(left,right):
            if self.alist[j] <= benchmark:
                i += 1
                self.alist[i],self.alist[j] = self.alist[j],self.alist[i]
        self.alist[i+1],self.alist[right] = self.alist[right],self.alist[i+1]    
        return i+1
    
    def QuickSort(self,left,right):
        if left < right:
            benchmark = self.Partition(left,right)
            self.QuickSort(left,benchmark - 1)
            self.QuickSort(benchmark + 1,right)
            
    def sort(self):    
        self.QuickSort(0,len(self.alist) - 1)
        
