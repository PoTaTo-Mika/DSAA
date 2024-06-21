import random as rd

class InsertSort():
    def __init__(self,alist):
        self.alist = alist
        
    def InsertSort(self):
        sorted_list = []
        sorted_list.append(self.alist[0])
        
        for i in range(1,len(self.alist)):
            temp = self.alist[i]
            insert = False
            for k in range(len(sorted_list)):
                if temp < sorted_list[k]:
                    sorted_list.insert(k,temp)
                    insert = True
                    break
                if not insert:
                    sorted_list.append(temp)
                    
        return sorted_list