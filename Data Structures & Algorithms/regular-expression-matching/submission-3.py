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

        m, n = len(p), len(s)
        memo = {}

        # i 是 p 的索引，j 是 s 的索引
        def dfs(i: int, j: int) -> bool:
            if i == m and j == n:
                return True

            # p 用完了，s 还有未匹配的，肯定不匹配
            if i > m-1:
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            # 判断后面是否有一个*字符
            # 如果是的话，这可以作为一个组，因为*的行为是受前序字符影响
            followed_by_asterisk = i+1<m and p[i+1]==asterisk

            if followed_by_asterisk:
                if j > n-1:
                    matched = dfs(i+2, j)
                
                # 普通字符匹配或万能字符
                elif p[i] == s[j] or p[i] == dot:
                    # 如果是一个'?*'组
                    # p[i] 会停留在普通字符
                    # 或直接跳过
                    matched = dfs(i, j+1) or dfs(i+2, j)
                
                # 不匹配，但好在是一个组，可以让该组消失
                else:
                    matched = dfs(i+2, j)
                
                memo[(i, j)] = matched

                return matched
            else:
                if j > n-1:
                    matched = False
                    
                elif p[i] == s[j] or p[i] == dot:
                    matched = dfs(i+1, j+1)
                else:
                    matched = False

                memo[(i, j)] = matched

                return matched


        return dfs(0, 0)
