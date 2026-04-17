class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1, len_2 = len(word1), len(word2)
        memo = {}
        
        def diff(m: int, n: int) -> int:
            # 两个 word 都结束了直接返回
            if m > len_1-1 and n > len_2-1:
                return 0
            # 任意 word 结束了，只能插入字符或者删除字符，不用继续递归，直接返回剩余长度
            elif m > len_1-1:
                return len_2-n
            elif n > len_2-1:
                return len_1-m

            if (m, n) in memo:
                return memo[(m, n)]

            c_1 = word1[m]
            c_2 = word2[n]
            
            min_ops = 0
            if c_1 == c_2:
                min_ops = diff(m+1, n+1)
            
            else:
                # c_1 和 c_2 不匹配，三种操作都有可能
                # 例子：
                #        0123456
                # word1="monkeys"
                # word2="money"
                #           . m==n==3时
                # （1）删除操作，1+diff(m+1,n)
                # （2）修改操作，1+diff(m+1,n+1)
                # （3）插入操作，1+diff(m,n+1)
                # 修改和插入操作本质上都是按照word2的字符对齐，然后继续递归
                # 差别是继续递归时的新起点
                # 需要注意的是，无论增删改字符，都不会对原word1做修改，所以len不变，索引也不变

                min_ops = 1+min(diff(m+1, n), diff(m+1, n+1), diff(m, n+1))
            
            memo[(m,n)] = min_ops
            return min_ops

        return diff(0, 0)