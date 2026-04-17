class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 符合条件的最少数量
        # 分解成两个方向来考虑：
        # 从左往右：如果右边孩子评分比左边高，右边孩子的糖数 = 左边孩子的糖数 + 1。
        # 从右往左：如果左边孩子评分比右边高，左边孩子的糖数 = 右边孩子的糖数 + 1。

        n = len(ratings)
        candy_dist = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy_dist[i] = candy_dist[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy_dist[i] = max(candy_dist[i], candy_dist[i+1] + 1)

        return sum(candy_dist)