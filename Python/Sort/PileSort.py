import random as rd
class PileSort():
    def __init__(self,alist):
        self.alist = alist
        self.n = len(alist)
        #[4,5,10,24,6]
    def build_max_pile(self):
        root_num = self.n//2-1
        for i in range(root_num,-1,-1): #完全二叉树的特性，叶子节点占一半
            self.heapify(self.n,i)
            
    def heapify(self,n,i):
        root = i
        left = 2*i + 1
        right = 2*i + 2
        # 如果左子节点存在且大于根节点
        if left < n and self.alist[i] < self.alist[left]:
            root = left
        # 如果右子节点存在且大于 root
        if right < n and self.alist[root] < self.alist[right]:
            root = right
        # 如果 root 不是根节点
        if root != i:
            self.alist[i], self.alist[root] = self.alist[root], self.alist[i]  # 交换
            # 递归地对受影响的子树进行 heapify
            self.heapify(n, root)
            
    def PileSort(self):
        self.build_max_pile()
        for i in range(self.n - 1, 0, -1):
            # 将当前根（最大值）移到数组末尾
            self.alist[i], self.alist[0] = self.alist[0], self.alist[i]
            # 调整剩余的堆
            self.heapify(i, 0)
        return self.alist
    

           