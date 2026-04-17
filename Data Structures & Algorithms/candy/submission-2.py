class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 要得到符合条件的最少数量，分解成两个方向来考虑：
        # 从左往右：如果右边评分比左边高，右边糖数 = 左边糖数+1
        # 从右往左：如果左边评分比右边高，左边糖数 = 右边糖数+1
        # 评分相同的情况下题目没有要求，但为了最少的分配数，就给最少值
        # 两次遍历，分别可以得到单向上满足条件的分配，但另一方向不确定
        # 所以最终取二者最大值，不会破坏原有单向的情况，得到双向满足条件的分配（左邻右舍）

        n = len(ratings)
        candy_dist = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy_dist[i] = candy_dist[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # 找到两个方向都满足条件的分配数量
                candy_dist[i] = max(candy_dist[i], candy_dist[i+1] + 1)

        # 最终candy_dist[i]是满足两个单向条件的最小值，求总和
        return sum(candy_dist)