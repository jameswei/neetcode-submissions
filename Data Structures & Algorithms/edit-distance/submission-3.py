class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 按照记忆化递归的解法来写dp 解法
        # 递归函数的参数是m 和n，它计算 word1[m:] 到 word2[n:] 的最小差
        # 递归函数不断深入直到遇到：
        # word1 或 word2 结束，就返回“未结束的 word 的剩余长度”
        # 这就是 base case，它是 dp 的初始状态或初始条件
        # 这就决定了dp 表格：
        # （1）要表示和递归函数同样的含义，两个参数m 和n 对应两个维度，[m][n]存储计算结果
        # （2）初始状态依靠 base case 先填充
        
        # 同时，递归函数中记忆化是在获得结果后更新，在新计算前查询
        # 记忆的内容是“更大m 和更大n”的计算结果，之后被用于“更小m 和更小n”的计算
        # 这决定了dp 表格的填充顺序也是从大到小：
        # （3）从表格右下角向左上角填充，也就是 [len(word1)][len(word2)] 向[0][0]
        
        INF = -1 * 2**31
        # 递归中，m和n 范围分别是[0,len_1-1] 和 [0, len_2-1]
        # 所以m 超出范围了，最小差距就是 len_2-n，同理n 超出范围了，最小差距是 len_1-m
        # 但是dp 表要将size设为 (m+1)*(n+1)
        # 其中多出来的[m][0,n-1]就表示m 超出了范围，这时差距是len_2-n，
        # 同理多出来的[0,m-1][n]表示n 超出了范围，这时差距是len_1-m
        m, n = len(word1), len(word2)
        dp = [[INF] * (n+1) for _ in range(m+1)]

        # dp[m][*] 和 dp[*][n]要提前处理
        # 最后一行
        for j in range(n):
            dp[m][j] = n-j
        
        # 最后一列
        for i in range(m):
            dp[i][n] = m-i

        dp[m][n] = 0

        # 从右下到左上
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    # 改字符，加字符，删字符
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])

        return dp[0][0]