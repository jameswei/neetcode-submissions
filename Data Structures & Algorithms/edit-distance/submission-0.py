class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1, len_2 = len(word1), len(word2)
        
        def diff(m: int, n: int) -> int:
            # 两个 word 都结束了直接返回
            if m > len_1-1 and n > len_2-1:
                return 0
            # 任意 word 结束了，只能 insert 或者 delete 操作，不用继续递归
            elif m > len_1-1:
                return len_2-n
            elif n > len_2-1:
                return len_1-m

            c_1 = word1[m]
            c_2 = word2[n]
            
            if c_1 == c_2:
                return 0 + diff(m+1, n+1)
            
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

            min_ops = min(diff(m+1, n), diff(m+1, n+1), diff(m, n+1))
            return 1 + min_ops

        return diff(0, 0)