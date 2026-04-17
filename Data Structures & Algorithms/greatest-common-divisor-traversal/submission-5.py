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
        
        union_find = UnionFind(n)

        # 先计算质数表
        max_num = max(nums)
        # 初始化除了0,1之外都是质数
        is_prime = [True] * (max_num+1)
        # 0,1不是质数
        is_prime[0] = is_prime[1] = False

        factor = 2
        while factor*factor <= max_num:
            # 如果是质数
            if is_prime[factor]:
                # 那么factor的倍数都不是质数，也就是那些合数都可被分解
                for composite in range(factor*factor, max_num+1, factor):
                    is_prime[composite] = False
            factor += 1

        # [2,√max_num]范围的所有质数
        primes = [p for p in range(len(is_prime)) if is_prime[p]]
        prime_to_idx = {}

        # 再用这些质数对每个num做质因分解
        for i in range(n):
            num = nums[i]

            for prime in primes:
                if num % prime == 0:
                    if prime in prime_to_idx:
                        union_find.union(i, prime_to_idx[prime])
                    else:
                        prime_to_idx[prime] = i
                    
                    # 一直除到底
                    while num % prime == 0:
                        num = num // prime
                
                # 接着就不需要像试除法一样递增factor
                # 而是直接用下一个prime去分解
        

        return union_find.count == 1