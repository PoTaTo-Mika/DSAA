from math import inf
import random as rd

class BucketSort():
    
    def __init__(self,alist):
        self.alist = alist
        self.totalnumber = len(alist)

    def create_bucket(self):
        big = -inf
        small = inf
        for num in self.alist:
            if num > big:
                big = num
            if num < small:
                small = num
        bucketnums = (big - small) // len(self.alist) + 1
        
        self.big = big
        self.small = small
        self.gap = (big - small) // len(self.alist) + 1  # 修正 gap 的计算方式
        
        return bucketnums
    
    def build_buckets(self):
        bucketnums = self.create_bucket()
        buckets = [[] for _ in range(bucketnums)]
        for num in self.alist:
            index = (num - self.small) // self.gap
            if index >= bucketnums:
                index = bucketnums - 1
            buckets[index].append(num)
        return buckets
    
    def BucketSort(self):
        bucket = self.build_buckets()
        nums = len(bucket)
        final = []
        for h in range(nums):
            bucket[h] = sorted(bucket[h])
            final += bucket[h]
        return final
                
arr = [rd.randint(1,100) for _ in range(20)]
print(arr)
bs = BucketSort(arr)
print(bs.BucketSort())
        