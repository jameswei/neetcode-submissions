class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
    
    def find(self, i: int) -> int:
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]
    
    def union(self, i: int, j: int):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if parent_i == parent_j:
            return

        # 按秩合并
        if self.rank[parent_i] < self.rank[parent_j]:
            self.parent[parent_i] = parent_j
        elif self.rank[parent_i] > self.rank[parent_j]:
            self.parent[parent_j] = parent_i
        else:
            # 只要等同秩的节点合并才更新秩
            self.parent[parent_j] = parent_i
            self.rank[parent_i] += 1
        
        self.count -= 1

        
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # 1个元素直接全连通
        if n == 1:
            return True
        
        # 1不是质数，它也没有质因数，所以必然无法和其他数值有公共质因数
        if 1 in nums:
            return False
        
        # 先计算质数表
        max_num = max(nums)
        # [2,max_num]范围每个数的最小质因数表
        spf = [0] * (max_num+1)

        factor = 2
        for factor in range(2, max_num+1):
            # 如果是质数
            if spf[factor] == 0:
                spf[factor] = factor

                # factor的倍数都不是质数，也就是那些合数都可被分解
                for composite in range(factor*factor, max_num+1, factor):
                    if spf[composite] == 0:
                        spf[composite] = factor
            
            factor += 1

        union_find = UnionFind(n)
        prime_to_idx = {}

        # 再用最小质因数对每个num做快速质因分解
        for i in range(n):
            num = nums[i]
            
            while num > 1:
                pf = spf[num]

                if pf in prime_to_idx:
                    union_find.union(i, prime_to_idx[pf])
                else:
                    prime_to_idx[pf] = i
                
                while num % pf == 0:
                    num = num // pf
                
                # 接着就不需要像试除法一样递增factor
                # 而是直接用剩余数值继续查表去分解

        return union_find.count == 1