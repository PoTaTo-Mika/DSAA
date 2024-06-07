import random as rd

class MergeSort():
    
    def __init__(self,alist):
        self.alist = alist
        self.help = []
        
    def Ms(self,alist):
        #首先切分数组
        if len(alist) <= 1:
            return alist
        
        mid = len(alist)//2
        left = self.Ms(alist[:mid])
        right = self.Ms(alist[mid:])
        
        return self.Merge(left,right)
    
    def Merge(self,left,right):
        sorted_list = []
        left_zz,right_zz = 0,0
        while left_zz < len(left) and right_zz < len(right):
            if left[left_zz] < right[right_zz]:
                sorted_list.append(left[left_zz])
                left_zz += 1
            else:
                sorted_list.append(right[right_zz])
                right_zz += 1
        
        for i in range(left_zz,len(left)):
            sorted_list.append(left[i])
        for i in range(right_zz,len(right)):
            sorted_list.append(right[i])
        '''
        extend方法：
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        '''
        return sorted_list
    
    def sort(self):
       self.alist = self.Ms(self.alist)
       return self.alist
