class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 朴素想法
        # 和“找s 中构成t 相同的子序列个数”问题不同：
        # 1.模式匹配中只确定存在性，不考虑个数，不用统计，找到任意一个有效解就结束。
        # 2.感觉对应方向相反，拿pattern去匹配source，类似于：
        #   pattern中有通配符.和*的存在，可以扩展出很多个字符串，从这些字符串中找到和source一样的。
        # 3.对应单个字符而言，即便因为有通配符存在也不可能将pattern直接展开成很多字符串，
        #   所以pattern中的单个字符没有“选和不选”的情况，而是“选1个和选几个”的情况。
        # 根据这些事实，感觉也是dfs解法，记忆化可以稍后优化

        dot, asterisk = ".", "*"
        wildcard = [dot, asterisk]

        m, n = len(p), len(s)

        # i 是 p 的索引，j 是 s 的索引
        def dfs(i: int, j: int) -> bool:
            if j > n-1:
                return True
            
            if i > m-1:
                return False
            
            char_p = p[i]
            char_s = s[j]

            # 是具体字符
            if char_p not in wildcard:
                # 且完全相同
                if char_p == char_s:
                    if dfs(i+1, j+1):
                        return True

            # 是通配符
            else:
                # 单字符通配符
                if char_p == ".":
                    if dfs(i+1, j+1):
                        return True

                # 任意通配符
                elif char_p == "*":
                    # 先检查前序字符p[i-1]
                    preceding = p[i-1]
                    if preceding not in wildcard:
                        if preceding == char_s:
                            if dfs(i, j+1):
                                return True
                    
                    else:
                        if dfs(i, j+1):
                            return True

            return False


        return dfs(0, 0)
