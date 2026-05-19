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
        def dfs(i: int, j: int, last_char: str, last_matched_char: str) -> bool:
            if j > n-1:
                return True
            
            if i > m-1:
                return False
            
            char_p = p[i]
            char_s = s[j]

            # 普通字符且相同
            if char_p == char_s:
                if dfs(i+1, j+1, char_p, char_p):
                    return True

            else:
                # 普通字符不相同
                if char_p not in wildcard:
                    # s[j] 还没匹配上，只能指望p[i+1]能以*来消除
                    if dfs(i+1, j, char_p, ""):
                        return True

                # 万能匹配
                elif char_p == dot:
                    if dfs(i+1, j+1, dot, char_s):
                        return True

                # * 特殊处理
                else:
                    # s[j] == s[j-1]
                    if last_matched_char == char_s:
                        # 可以扩展次数
                        if dfs(i, j+1, last_char, last_matched_char):
                            return True
                    
                    # 没法扩展次数，但是前面是万能字符
                    elif last_char == dot:
                        #  还能再用一次万能匹配
                        if dfs(i, j+1, last_char, last_matched_char):
                            return True

                    else:
                        # s[j] != s[j-1] *帮不上忙了
                        if dfs(i+1, j, asterisk, last_matched_char):
                            return True

            return False

        return dfs(0, 0, "", "")
