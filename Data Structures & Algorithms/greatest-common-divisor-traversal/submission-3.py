class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self, i: int) -> int:
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]
    
    def union(self, i: int, j: int):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if parent_i != parent_j:
            self.parent[j] = i
            self.count -= 1

        
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # gcd最大公因数
        # traverse between i and j, i!=j and gcd(nums[i],nums[j])>1，这句话代表i和j之间可以“走通”，也就是i和j之间有条边
        # 也就是nums[]代表一些节点，[i]...[j]是其中两个节点，如果gcd([i],[j])说明节点右边（无向）
        # 原问题是判断是否所有的pair之间可以走通，也就是问所有成对的节点是否有边，这就转化成图的连通性问题
        # 图的动态连通性问题，用union-find解最高效，在逐步建图（加边）后，最终判断所有节点是否属于同一个连通量

        # 但对于给定nums遍历所有的pair找求gcd()的话，至少需要n^2的复杂度
        # 再借助质因数和最大公约数的概念，转化成将每个数分解质因数，最终根据公共质因数来建立连通性（也就是说[i]和[j]存在公共质因数，那一定满足gcd([i],[j])>1的条件
        # 这样方式下可以将时间复杂度降到n
        n = len(nums)
        
        # 1个元素直接全连通
        if n == 1:
            return True
        
        # 1不是质数，它也没有质因数，所以必然无法和其他数值有公共质因数
        if 1 in nums:
            return False
        
        union_find = UnionFind(n)

        prime_to_idx = {}

        for i in range(n):
            num = nums[i]
            
            # 试除法分解质因数
            factor = 2
            while factor <= math.sqrt(num):
                if num % factor == 0:
                    if factor in prime_to_idx:
                        union_find.union(i, prime_to_idx[factor])
                    else:
                        prime_to_idx[factor] = i
                    
                    while num % factor == 0:
                        num = num // factor
            
                factor += 1

            if num > 1:
                if num in prime_to_idx:
                    union_find.union(i, prime_to_idx[num])
                else:
                    prime_to_idx[num] = i

        return union_find.count == 1